import json
from machine import Pin, Timer
import time
import manchester
import uasyncio
from ubinascii import hexlify, unhexlify

import rfm69

NETWORKID = 0x0116251c # change this
IS_RFM69HW      = True

# utils
def invert_b(x):
  return x ^ 0xFF

def invert(buf):
  return bytearray(map(invert_b, buf))

def crc8(msg, poly=1):
  crc = 0
  for byte in msg:
    crc ^= byte
    for _ in range(8):
      if crc & 0x80:
        crc = ((crc << 1) ^ poly) & 0xFF
      else:
        crc = (crc << 1) & 0xFF

  return crc

class Heat:
  def __init__(self):
    self.radio = rfm69.RFM69(isRFM69HW=IS_RFM69HW, csPin=15, intPin=5, rstPin=4, debug=False)
    self.network_id = NETWORKID
    self.network = [
      (self.network_id >> 24) & 0xFF,
      (self.network_id >> 16) & 0xFF,
      (self.network_id >> 8) & 0xFF,
      self.network_id & 0xFF,
    ]
    self.radio.initialize()
    self.radio._data_cb = self.handle_frame
    self.radio.listen()
    self.wait_ack = []

    self.cbs = {}
 
  def _find_waiter(self, addr):
    for _addr, ack_waiter in self.wait_ack:
      if _addr == addr:
        return ack_waiter
   
  def sendFrameSync(self, from_addr, to_addr, typ, payload):
    frame_len = len(payload) + 10
    frame = [
      (self.network_id >> 24) & 0xFF,
      (self.network_id >> 16) & 0xFF,
      (self.network_id >> 8) & 0xFF,
      self.network_id & 0xFF,
      from_addr,
      typ,
      (frame_len >> 16) & 0xFF,
      frame_len & 0xFF,
      to_addr,
    ] + payload

    with_crc = bytearray(frame + [crc8(frame) ^ 0xFF])

    print('send out', hexlify(bytearray(with_crc), ':'))

    # print('send', list(map(hex, with_crc)))
    raw = invert(manchester.encode(with_crc))
    # print('raw frame', list(map(hex, invert(raw))))
    self.radio.send(raw) 

  async def sendFrame(self, from_addr, to_addr, typ, data, ack=True):
    if not ack:
      print('send frame with no ack to', to_addr)
      return self.sendFrameSync(from_addr, to_addr, typ, data)
 
    try:
      ack_waiter = self._find_waiter(from_addr)
      if ack_waiter:
        await uasyncio.wait_for(ack_waiter.wait(), 2)
    except uasyncio.TimeoutError:
      print('previous call stalled, abort', from_addr, ack_waiter)
      return False

    ack_waiter = uasyncio.ThreadSafeFlag()
    pair = ([from_addr, ack_waiter])
    self.wait_ack.append(pair)

    retry = 15
    while retry > 0:
      self.sendFrameSync(from_addr, to_addr, typ, data)
      print('sent frame to', to_addr)
      try:
        await uasyncio.wait_for(ack_waiter.wait(), 0.3)
        self.wait_ack.remove(pair)
        return True
      except uasyncio.TimeoutError:
        retry -= 1

    print('sending frame timed out to', from_addr)
    self.wait_ack.remove(pair)
    return False

  def ping(self, zone):
    buf = [0xFF, 0x01, 0x01, 0x49, 0x0C, 0x00, 0xF0, 0xF0, 0x72, 0xF0, 0xFF ^ zone ^ 4]
    self.sendCommand(zone, 0xFF, 0x0113, buf, False)

  def temp(self):
    buf = [
      0x05, 0x41, 0x00, 0x1c,
      0x01, 0xF0, 0x81, 0x92, 0x00, 0x35,
      0x91, 0x03, 0x00, 0x08, 0xe2,
      0x14, 0x11, 0x14, 0x14,
      0x34, 0x7f, 0x91, 0xb6, 0x4f
    ]
    self.sendFrame(buf)

  def ack(self):
    buf = [
       0x05, 0x03, 0x00, 0x0A, 0x01, 0x01 ^ 0x05 | 0xD8]
    self.sendFrame(buf)

  def conf13(self, zone):
    pass
    """
    process data paclet 1 3 0x13 het b'f0:80:13:01:00:00:03:e8:0b:b8:08:02:00:00:15:9b:0e:04:9a'
    process data paclet 1 3 0x13 off b'f0:80:93:01:00:00:03:e8:0b:b8:08:02:00:00:15:21:c7:6e:c7'
    process data paclet 1 2 0x13 off b'f0:80:93:01:00:00:03:e8:0b:b8:08:02:00:00:15:21:c7:6e:c7'
    process data paclet 1 2 0x13 het b'f0:80:13:01:00:00:03:e8:0b:b8:08:02:00:00:15:9b:0e:04:9a'

    """

  def get_group(self, zone):
    group = 0x30 | zone
    if zone == 8:
      group = 0x35
    return group

  def conf14(self, zone, override=None):
    buf = [ 0xf0, 0x25, 0x8a, 0x00, 0x03, self.get_group(zone) ]
    code = unhexlify(b'01020304')
    return self.sendCommand(zone, 1, 0x4114, buf + code)

  def conf11(self):
    buf = [
      0x05, 0x41, 0x00, 0x11, 0x01,
      0x01, 0x15, 0x01, 
      0x00, 0x00, 0x00, 0x00,
      0x90
    ]
    self.sendFrame(buf)

  # Ask sensor what current temp is
  def query_current(self, zone):
    """
    process data paclet 1 3 0x13 het b'f0:80:13:01:00:00:03:e8:0b:b8:08:02:00:00:15:9b:0e:04:9a'
    process data paclet 1 3 0x13 off b'f0:80:93:01:00:00:03:e8:0b:b8:08:02:00:00:15:21:c7:6e:c7'
    """
    seq = 1 << 7
    buf = [
      0xf0, 0x81, seq | 0x13, 0x01, 0, 0,
      0x03, 0xe8, 0x0b, 0xb8, 0x08, 0x02, 0, 0,
      0x15
    ]
    code = unhexlify(b'21c76ec7')
    return self.sendFrame(1, zone, 0x41, buf + list(code))

  # Ask main unit what target temp is set on given zone
  def query_target(self, zone):
    # nodeid 8 'f0:81:94:00:35:a8:03:02:03:03:14:00:14:11:14:15:30:03:ea:b9'
    # nodeid 8 'f0:81:14:00:35:a8:03:02:03:03:14:00:14:11:14:15:75:12:bc:ff'
    # nodeid 6 'f0:81:94:00:36:a8:03:02:03:03:14:00:14:11:14:15:45:44:3c:25''
    # nodeid 6 'f0:81:14:00:36:a8:03:02:03:03:14:00:14:11:14:15:4e:02:2f:48'
    # nodeid 4 'f0:81:14:00:34:a8:03:02:03:03:14:00:14:11:14:15:75:9a:9a:bf''
    # nodeid 4 'f0:81:94:00:34:a8:03:02:03:03:14:00:14:11:14:15:eb:e9:03:65'
    # nodeid 2 'f0:81:14:00:32:a8:03:02:03:03:14:00:14:11:14:15:03:ca:c0:15'
    # nodeid 2 'f0:81:94:00:32:a8:03:02:03:03:14:00:14:11:14:15:b3:dc:d5:3f'
    # nodeid 3 'f0:81:14:00:33:a8:03:02:03:03:14:00:14:11:14:15:16:1a:c6:3d'
    # nodeid 3 'f0:81:94:00:33:a8:03:02:03:03:14:00:14:11:14:15:86:96:5a:f1'

    seq = 0 << 7
    buf = [
      0xf0, 0x81, seq | 0x14, 0x00, self.get_group(zone),
      0xA8, 0x03, 0x02, 0x03, 0x03,
      0x14, 0x00, 0x14, 0x11, 0x14, 0x15,
    ]
    codes = {
      0x02: b'03cac015',
      0x03: b'161ac63d',
      0x04: b'759a9abf',
      0x06: b'4e022f48',
      0x08: b'7512bcff',
    }
    code = unhexlify(codes.get(zone) or b'01020304')

    return self.sendFrame(zone, 1, 0x41, buf + list(code))

  def set_temp(self, zone=8, target=20):
    # process data paclet 8 1 0xe het b'f0:81:0e:00:35:01:03:01:04:b0:27:6b:04:d7' 12
    # process data paclet 8 1 0xe het b'f0:81:0e:00:35:01:03:01:08:98:e7:fc:49:88' 22

    # process data paclet 8 1 0xe off b'f0:81:8e:00:35:01:03:01:04:b0:09:77:c1:03' 12
    # process data paclet 8 1 0xe off b'f0:81:8e:00:35:01:03:01:08:98:a3:e8:e7:27' 22
    # process data paclet 8 1 0xe off b'f0:81:8e:00:35:01:03:01:07:d0:df:c7:b0:d5' 20
    # process data paclet 8 1 0xe off b'f0:81:8e:00:35:01:03:01:08:fc:ba:aa:c4:28' 23
    # process data paclet 8 1 0xe off b'f0:81:8e:00:35:01:03:01:09:60:9a:40:0d:3a' 24

    # process data paclet 6 1 0xe off b'f0:81:8e:00:36:01:03:01:07:08:27:5a:d5:16'
    # process data paclet 6 1 0xe off b'f0:81:8e:00:36:01:03:01:06:40:2a:50:fd:89'
    # process data paclet 6 1 0xe off b'f0:81:8e:00:36:01:03:01:04:b0:3b:cb:f7:8b'
    # process data paclet 6 1 0xe off b'f0:81:8e:00:36:01:03:01:05:78:a4:ab:30:bf'
    # process data paclet 6 1 0xe off b'f0:81:8e:00:36:01:03:01:07:d0:84:0c:85:25'
    # process data paclet 6 1 0xe off b'f0:81:8e:00:36:01:03:01:08:98:2d:fd:ea:d6'
    # process data paclet 6 1 0xe off b'f0:81:8e:00:36:01:03:01:09:60:db:b7:6a:6d'
    # process data paclet 6 1 0xe off b'f0:81:8e:00:36:01:03:01:08:fc:e3:23:a7:5e'

    # process data paclet 4 1 0xe off b'f0:81:8e:00:34:01:03:01:07:d0:2f:21:a0:d1'
    # process data paclet 4 1 0xe off b'f0:81:8e:00:34:01:03:01:08:98:4b:bb:6e:17'
    # process data paclet 4 1 0xe off b'f0:81:8e:00:34:01:03:01:09:60:4d:d1:41:e3'
    # process data paclet 4 1 0xe off b'f0:81:8e:00:34:01:03:01:04:b0:36:94:84:81'

    seq = 1 << 7
    codes = {
      0x0804b0: b'0977c103',
      0x0807d0: b'dfc7b0d5',
      0x080898: b'a3e8e727',
      0x0808fc: b'baaac428',
      0x080960: b'9a400d3a',

      0x0604b0: b'3bcbf78b',
      0x060578: b'a4ab30bf',
      0x0607d0: b'840c8525',
      0x060898: b'2dfdead6',
      0x0608fc: b'e323a75e',
      0x060960: b'dbb76a6d',

      0x0404b0: b'36948481',
      0x0407d0: b'2f21a0d1',
      0x040898: b'4bbb6e17',
      0x040960: b'4dd141e3',
    }

    target = int(target) # TODO
    target_l = (target * 100) & 0xFF
    target_h = ((target * 100) >> 8) & 0xFF

    code_key = zone << 16 | target_h << 8 | target_l
    print('code key', hex(code_key));
    code = unhexlify(codes.get(code_key) or b'01020304')

    buf = [
      0xf0, 0x81, seq | 0x0e, 0x00, self.get_group(zone),
      0x01, 0x03, 0x01, 
    ] + [target_h, target_l, ] + list(code)

    return self.sendFrame(zone, 1, 0x41, buf)

  def handle_frame(self, raw):
    data = manchester.decode(invert(raw))
    if len(data) < 10:
      print('ignore short packet', data)
      return

    net_id = (data[0] << 24) | (data[1] << 16) | (data[2] << 8) | data[3]
    from_addr = data[4]
    typ = data[5]
    to_addr = data[8]
    payload = data[9:-1]
    expected_len = data[7]

    if net_id != self.network_id:
      print('address code mismatch', hex(net_id))
      return

    len_ok = len(data) == expected_len
    crc_ok = (crc8(data[:-1]) ^ 0xFF) == data[-1]

    if not len_ok or not crc_ok:
      return

    if typ == 0x03:
      return self.handle_ack(from_addr, to_addr)
    elif typ == 0x41:
      return self.handle_data(from_addr, to_addr, payload)

  def handle_data(self, from_addr, to_addr, data):
    state = 'off' if data[2] & 0x80 else 'heat'
    cmd = data[2] & 0x7F
    direction = 'up' if data[1] & 0x81 else 'down'
    payload = data[3:-4]

    print('process data paclet', from_addr, to_addr, hex(cmd), state, hexlify(data, ':'))

    if cmd == 0x12:
      return self.handle_current_temp(from_addr, to_addr, payload)
    if cmd == 0x0E:
      return self.handle_set_temp(from_addr, to_addr, payload)
    if cmd == 0x0D:
      return self.handle_state(from_addr, to_addr, payload, state)
    if cmd == 0x13:
      return self.handle_target_info(from_addr, to_addr, payload, state)
    else:
      print('ignore packet', from_addr, to_addr, state, cmd, payload)
    
  def handle_current_temp(self, from_addr, to_addr, data):
    temp_c = (data[5] << 8 | data[6]) / 100
    self.propagate(from_addr, 'temp', temp_c)

  def handle_set_temp(self, from_addr, to_addr, data):
    temp_c = (data[5] << 8 | data[6]) / 100
    self.propagate(from_addr, 'target_temp', temp_c)

  def handle_target_info(self, from_addr, to_addr, data, state):
    temp_c = (data[7] << 8 | data[8]) / 100
    self.propagate(to_addr, 'target_temp', temp_c)
    # await self.propagate(to_addr, 'state', state) this is wrong

  def handle_state(self, from_addr, to_addr, data, state):
    # await self.propagate(to_addr, 'state', state)
    pass

  def handle_ack(self, from_addr, to_addr):
    print('got ack to', to_addr)
    ack_waiter = self._find_waiter(to_addr)
    if ack_waiter:
      ack_waiter.set()

  def propagate(self, zone, event, data):
    # will be overwritten by main.py
    pass

  async def _propagate(self, zone, event, data):
    cb = self.cbs.get(zone)
    if not cb:
      return
    await cb(event, data)

  def start(self):
    pass

  def subscribe(self, zone, cb):
    self.cbs[zone] = cb
