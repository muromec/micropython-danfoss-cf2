import json
from machine import Pin, Timer
import time
import manchester
import uasyncio
from ubinascii import hexlify

import rfm69

FREQUENCY   = rfm69.RF69_868MHZ
NODEID = 9
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
    self.radio._data_cb = lambda x: x
    self.radio.listen()
    self.wait_ack = []

    self.cbs = {}
    
  def sendFrame(self, buf):
    with_crc = bytearray(buf + [crc8(buf) ^ 0xFF])
    # print('send', list(map(hex, with_crc)))
    raw = invert(manchester.encode(with_crc))
    # print('raw frame', list(map(hex, invert(raw))))
    self.radio.send(raw) 

  def _find_waiter(self, addr, cmd=None):
    for _addr, _cmd, ack_waiter in self.wait_ack:
      if _addr == addr and (cmd is None or cmd == _cmd):
        return ack_waiter

  async def sendCommand(self, from_addr, to_addr, op_code, data, ack=True):
    op_code_h = op_code >> 8
    op_code_l = op_code & 0xFF
    packet = self.network + [from_addr, op_code_h, 0, op_code_l, to_addr] + data
   
    if not ack:
      print('send frame with no ack to', to_addr)
      return self.sendFrame(packet)
 
    try:
      ack_waiter = self._find_waiter(from_addr, cmd=None)
      if ack_waiter:
        await uasyncio.wait_for(ack_waiter.wait(), 2)
    except uasyncio.TimeoutError:
      print('previous call stalled, abort', from_addr, ack_waiter)
      return False

    ack_waiter = uasyncio.Event()
    tri = ([from_addr, op_code, ack_waiter])
    self.wait_ack.append(tri)

    retry = 15
    while retry > 0:
      self.sendFrame(packet)
      print('sent frame to', to_addr)
      try:
        await uasyncio.wait_for(ack_waiter.wait(), 0.3)
        self.wait_ack.remove(tri)
        return True
      except uasyncio.TimeoutError:
        retry -= 1

    print('sending opcode timed out with no ack', hex(op_code), from_addr)
    self.wait_ack.remove(tri)
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

  def conf14(self, zone, override=None):
    buf = [ 0xf0, 0x25, 0x8a, 0x00, 0x03, 0x30 | zone ]
    code = override  or [1, 2, 3, 4]
    return self.sendCommand(zone, 1, 0x4114, buf + code)

  def conf11(self):
    buf = [
      0x05, 0x41, 0x00, 0x11, 0x01,
      0x01, 0x15, 0x01, 
      0x00, 0x00, 0x00, 0x00,
      0x90
    ]
    self.sendFrame(buf)

  def conf1e(self):
    buf = [
      0x05, 0x41, 0x00, 0x1e, 0x01,
      0xf0, 0x81, 0x14, 0x00, 0x35,
      0xA8, 0x03, 0x02, 0x03, 0x03,
      0x14, 0x00, 0x14, 0x11, 0x14, 0x15,
      0x72, 0x12, 0xbc, 0xFF, 0x47
    ]
    self.sendFrame(buf)

  def set_temp(self, num=5, target=20, d2=0xE, code=[1,2,3,4]):
    target = int(target) # TODO
    target_l = (target * 100) & 0xFF
    target_h = ((target * 100) >> 8) & 0xFF

    buf = [
      0xf0, 0x81, d2 | 0x0e, 0x00, 0x30 | num,
      0x01, 0x03, 0x01, 
    ] + [target_h, target_l, ] + code[:4]

    return self.sendCommand(num, 1, 0x4118, buf)

  async def handle_frame(self, raw):
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
      return await self.handle_ack(from_addr, to_addr)
    elif typ == 0x41:
      return await self.handle_data(from_addr, to_addr, payload)

  async def handle_data(self, from_addr, to_addr, data):
    state = 'off' if data[2] & 0x80 else 'heat'
    cmd = data[2] & 0x7F
    direction = 'up' if data[1] & 0x81 else 'down'
    payload = data[3:-4]

    print('process data paclet', from_addr, to_addr, hex(cmd), state, hexlify(data, ':'))

    if cmd == 0x12:
      return await self.handle_current_temp(from_addr, to_addr, payload)
    if cmd == 0x0E:
      return await self.handle_set_temp(from_addr, to_addr, payload)
    if cmd == 0x0D:
      return await self.handle_state(from_addr, to_addr, payload, state)
    if cmd == 0x13:
      return await self.handle_target_info(from_addr, to_addr, payload, state)
    else:
      print('ignore packet', from_addr, to_addr, state, cmd, payload)
    
  async def handle_current_temp(self, from_addr, to_addr, data):
    temp_c = (data[5] << 8 | data[6]) / 100
    await self.propagate(from_addr, 'temp', temp_c)

  async def handle_set_temp(self, from_addr, to_addr, data):
    temp_c = (data[5] << 8 | data[6]) / 100
    await self.propagate(from_addr, 'target_temp', temp_c)

  async def handle_target_info(self, from_addr, to_addr, data, state):
    temp_c = (data[7] << 8 | data[8]) / 100
    await self.propagate(to_addr, 'target_temp', temp_c)
    # await self.propagate(to_addr, 'state', state) this is wrong

  async def handle_state(self, from_addr, to_addr, data, state):
    # await self.propagate(to_addr, 'state', state)
    pass

  async def handle_ack(self, from_addr, to_addr):
    print('got ack to', to_addr)
    ack_waiter = self._find_waiter(to_addr, cmd=None)
    if ack_waiter:
      ack_waiter.set()

  async def propagate(self, zone, event, data):
    cb = self.cbs.get(zone)
    if not cb:
      return
    await cb(event, data)

  def start(self):
    pass

  def subscribe(self, zone, cb):
    self.cbs[zone] = cb
