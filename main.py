import uasyncio
import config
import time
import machine
from machine import Timer

from heat import Heat
from adapter import Adapter
import umqttsimple
import wrapq
 
def panic(f):
  def wrapped(*a):
    try:
      return f(*a)
    except Exception as e:
      print('failure in', f)
      import sys
      sys.print_exception(e)
      machine.reset()

  return wrapped

async def main():
  h = Heat()
  mqtt = umqttsimple.MQTTClient(*config.mqtt_config)
  h.propagate = panic(wrapq.wrap(h._propagate))

  await mqtt.connect()

  for zone in [2, 3, 4, 6, 8]: ## autodiscover
    adapter = Adapter(mqtt, h, zone_id=zone)
    await adapter.link()

  print('process mqtt events')
  while True:
    await mqtt.wait_msg()

async def wd():
  timer = Timer(0)
  last_tick = time.ticks_ms()
  def check(timer):
    lag = (time.ticks_ms() - last_tick) / 5_000
    if lag > 1.5:
      print('lag', lag)
    if lag > 10:
      print('watchdog detected a stall of ', lag, last_tick, time.ticks_ms())
      machine.reset()
    
  timer.init(period=10_000,  mode=Timer.PERIODIC, callback=check)

  while True:
    await uasyncio.sleep_ms(5_000)
    last_tick = time.ticks_ms()
    #await mqtt.ping()

@panic
def run():
  loop = uasyncio.get_event_loop()
  loop.run_until_complete(uasyncio.gather(main(), wd()))
  machine.reset()

run()
