import uasyncio
import time

async def process_events(fn, flag, qu):
  while True:
    while qu:
      await fn(*qu.pop())

    await flag.wait()

def wrap(fn):
  wake_flag = uasyncio.ThreadSafeFlag()
  q_lock = uasyncio.Lock()
  event_q = []

  def wrapped(*a, **kw):
    event_q.append(a)
    wake_flag.set()

  loop = uasyncio.get_event_loop()
  loop.create_task(
    process_events(fn, wake_flag, event_q)
  )

  return wrapped
