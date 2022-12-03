import time
import ustruct as struct
from ubinascii import hexlify
import uasyncio

class MQTTException(Exception):
    pass

def locked(lock, op_name):
  def decorator(f):
    async def wrapped(*a):
      print('mqtt op', op_name, 'need a lock')
      await lock.acquire()
      try:
        return await f(*a)
      finally:
        print('mqtt op', op_name, 'lock release')
        lock.release()
    return wrapped

  return decorator

class MQTTClient:

    lock = uasyncio.Lock()

    def __init__(self, client_id, server, port=1883, user=None, password=None, keepalive=0):
        self.client_id = client_id
        self.server = server
        self.port = port
        self.pid = 0
        self.cbs = []
        self.user = user
        self.pswd = password
        self.keepalive = keepalive
        self.lw_topic = None
        self.lw_msg = None
        self.lw_qos = 0
        self.lw_retain = False

    async def _send_str(self, s):
        self.writeS.write(struct.pack("!H", len(s)))
        self.writeS.write(s)
        await self.writeS.drain()

    async def _write(self, b):
        self.writeS.write(b)
        await self.writeS.drain()

    async def _read(self, n):
        ret = await self.readS.readexactly(n)
        return ret
        
    async def _recv_len(self):
        n = 0
        sh = 0
        while 1:
            buf = await self._read(1)
            b = buf[0]
            n |= (b & 0x7f) << sh
            if not b & 0x80:
                return n
            sh += 7

    def set_callback(self, f):
        self.cbs.append(f)

    async def notify_sub(self, topic, msg):
        for cb in self.cbs:
            try:
                await cb(topic, msg)
            except Exception as e:
                print('failed process callback for', topic, msg)
                import sys
                sys.print_exception(e)

    def set_last_will(self, topic, msg, retain=False, qos=0):
        assert 0 <= qos <= 2
        assert topic
        self.lw_topic = topic
        self.lw_msg = msg
        self.lw_qos = qos
        self.lw_retain = retain

    async def connect(self, clean_session=True):
        self.readS, self.writeS = await uasyncio.open_connection(self.server, self.port)
        premsg = bytearray(b"\x10\0\0\0\0\0")
        msg = bytearray(b"\x04MQTT\x04\x02\0\0")

        sz = 10 + 2 + len(self.client_id)
        msg[6] = clean_session << 1
        if self.user is not None:
            sz += 2 + len(self.user) + 2 + len(self.pswd)
            msg[6] |= 0xC0
        if self.keepalive:
            assert self.keepalive < 65536
            msg[7] |= self.keepalive >> 8
            msg[8] |= self.keepalive & 0x00FF
        if self.lw_topic:
            sz += 2 + len(self.lw_topic) + 2 + len(self.lw_msg)
            msg[6] |= 0x4 | (self.lw_qos & 0x1) << 3 | (self.lw_qos & 0x2) << 3
            msg[6] |= self.lw_retain << 5

        i = 1
        while sz > 0x7f:
            premsg[i] = (sz & 0x7f) | 0x80
            sz >>= 7
            i += 1
        premsg[i] = sz

        await self._write(premsg[:i + 2])
        await self._write(msg)

        #print('connect', hex(len(msg)), hexlify(msg, ":"))

        await self._send_str(self.client_id)
        if self.lw_topic:
            await self._send_str(self.lw_topic)
            await self._send_str(self.lw_msg)
        if self.user is not None:
            await self._send_str(self.user)
            await self._send_str(self.pswd)
        resp = await self.readS.readexactly(4)
        assert resp[0] == 0x20 and resp[1] == 0x02
        if resp[3] != 0:
            raise MQTTException(resp[3])
        return resp[2] & 1

    def disconnect(self):
        await self._write(b"\xe0\0")
        self.readS.close()
        self.writeS.close()

    @locked(lock, 'ping')
    async def ping(self):
        print('ping')
        await self._write(b"\xc0\0")

    @locked(lock, 'pub')
    async def publish(self, topic, msg, retain=False, qos=0):
        pkt = bytearray(b"\x30\0\0\0")
        pkt[0] |= qos << 1 | retain
        sz = 2 + len(topic) + len(msg)
        if qos > 0:
            sz += 2
        assert sz < 2097152
        i = 1
        while sz > 0x7f:
            pkt[i] = (sz & 0x7f) | 0x80
            sz >>= 7
            i += 1
        pkt[i] = sz
        #print('publish', hex(len(pkt)), hexlify(pkt, ":"), i)
        await self._write(pkt[:i+1]) #, i + 1) num bytes to write
        await self._send_str(topic)
        if qos > 0:
            self.pid += 1
            pid = self.pid
            struct.pack_into("!H", pkt, 0, pid)
            await self._write(pkt[:2])
        await self._write(msg)
        if qos == 1:
            while 1:
                op = await self.wait_msg()
                if op == 0x40:
                    sz = await self._read(1)
                    assert sz == b"\x02"
                    rcv_pid = await self._read(2)
                    rcv_pid = rcv_pid[0] << 8 | rcv_pid[1]
                    if pid == rcv_pid:
                        return
        elif qos == 2:
            assert 0

    @locked(lock, 'sub')
    async def subscribe(self, topic, qos=0):
        pkt = bytearray(b"\x82\0\0\0")
        self.pid += 1
        struct.pack_into("!BH", pkt, 1, 2 + 2 + len(topic) + 1, self.pid)
        #print('s', hex(len(pkt)), hexlify(pkt, ":"))
        await self._write(pkt)
        await self._send_str(topic)
        await self._write(qos.to_bytes(1, "little"))
        while 1:
            op = await self.wait_msg()
            if op == 0x90:
                resp = await self._read(4)
                #print(resp)
                assert resp[1] == pkt[2] and resp[2] == pkt[3]
                if resp[3] == 0x80:
                    raise MQTTException(resp[3])
                return

    # Wait for a single incoming MQTT message and process it.
    # Subscribed messages are delivered to a callback previously
    # set by .set_callback() method. Other (internal) MQTT
    # messages processed internally.
    async def wait_msg(self):
        print('wait msg...', time.ticks_cpu())
        res = await self._read(1)
        print('mqtt got', res[0] if res else res)
        if res is None:
            return None
        if res == b"":
            raise OSError(-1)
        if res == b"\xd0":  # PINGRESP
            buf = await self._read(1)
            sz = buf[0]
            assert sz == 0
            print('got pong')
            return None

        op = res[0]
        if op & 0xf0 != 0x30:
            return op

        @locked(self.lock, 'read msg')
        def helper():
        
            sz = await self._recv_len()
            topic_len = await self._read(2)
            topic_len = (topic_len[0] << 8) | topic_len[1]
            topic = await self._read(topic_len)
            sz -= topic_len + 2
            if op & 6:
                pid = await self._read(2)
                pid = pid[0] << 8 | pid[1]
                sz -= 2

            msg = await self._read(sz)
            print('got msg', topic, msg)

            if op & 6 == 2:
                pkt = bytearray(b"\x40\x02\0\0")
                print('do mqtt ack')
                struct.pack_into("!H", pkt, 2, pid)
                await self._write(pkt)
            elif op & 6 == 4:
                assert 0

            return topic, msg
          
        topic, msg = await helper()
        await self.notify_sub(topic, msg)
