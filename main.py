import uasyncio
import config
import time
import machine

from heat import Heat
from adapter import Adapter
import umqttsimple
 
print('starting radio')
h = Heat()

mqtt = umqttsimple.MQTTClient(*config.mqtt_config)

radio_flag = uasyncio.ThreadSafeFlag()
radio_lock = uasyncio.Lock()
radio_q = []

def radio_frame(data):
  radio_q.append(data)
  radio_flag.set()
  print('got radio', time.ticks_cpu(), 'q size', len(radio_q))

h.radio._data_cb = radio_frame

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
  await mqtt.connect()

  for zone in [2, 3, 4, 6, 8]: ## autodiscover
    adapter = Adapter(mqtt, h, zone_id=zone)
    await adapter.link()

  print('process mqtt events')
  while True:
    await mqtt.wait_msg()

@panic
async def radio_events():
  while True:
    while radio_q:
      await h.handle_frame(radio_q.pop())

    print('wait for next even..', time.ticks_cpu())
    await radio_flag.wait()

async def tick():
  while True:
    await uasyncio.sleep_ms(5000)
    print('tick...', time.ticks_cpu())
    #await mqtt.ping()

@panic
def run():
  loop = uasyncio.get_event_loop()
  loop.run_until_complete(uasyncio.gather(main(), radio_events(), tick()))
  machine.reset()

run()
