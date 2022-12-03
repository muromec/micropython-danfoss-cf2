import ujson
from machine import Timer

def topic(path):
  def getter(self):
    return self.topic_prefix+path

  return property(getter)

class Adapter:
  def __init__(self, mqtt, heat, zone_id):
    self.mqtt = mqtt
    self.heat = heat
    self.zone = zone_id
    self.last_speed = None

  @property
  def topic_prefix(self):
    return 'homeassistant/climate/{}/{}'.format(hex(self.heat.network_id), self.zone)

  mode_topic = topic('/state')
  set_mode_topic = topic('/state/set')
  
  temp_topic = topic('/temp')
  set_temp_topic = topic('/temp/set')
  target_temp_topic = topic('/temp/target')

  config_topic = topic('/config')

  @property
  def config_data(self):
    return {
      'name': 'Heater {}@{}'.format(self.zone, hex(self.heat.network_id)),
      'unique_id': 'danfoss_{}@{}'.format(self.zone, hex(self.heat.network_id)),
      'mode_command_topic': self.set_mode_topic,
      'mode_state_topic': self.mode_topic,
      'current_temperature_topic': self.temp_topic,
      'temperature_command_topic': self.set_temp_topic,
      'temperature_state_topic': self.target_temp_topic,
      'temperature_unit': 'C',
      'modes': ['off', 'heat'],
    }
      
  async def link(self):
    self.heat.subscribe(self.zone, self.handle_event)

    self.mqtt.set_callback(self.handle_mqtt)
    await self.mqtt.subscribe(self.set_mode_topic)
    await self.mqtt.subscribe(self.set_temp_topic)
    print('subscribed to mqtt')

    data = ujson.dumps(self.config_data)
    await self.mqtt.publish(self.config_topic, data)
    print('advertise to mqtt')

  async def handle_mqtt(self, topic, msg):
    topic_str = str(topic, 'latin')
    msg = str(msg, 'latin')
    print('mqtt', topic_str, msg)
    # setting mode and temperature does not work
    if topic_str == self.set_mode_topic:
      await self.heat.conf14(self.zone)
      if msg == 'heat':
        await self.heat.set_temp(self.zone, 24)
      else:
        await self.heat.set_temp(self.zone, 12)
    elif topic_str == self.set_temp_topic:
      print('set temp to', msg, 'on', self.zone)

      try:
        await self.heat.conf14(self.zone)
        is_ok = await self.heat.set_temp(self.zone, float(msg))
        if is_ok:
          await self.handle_event('target_temp', int(float(msg)))
      except Exception as e:
        print('failed to set temp', self.zone, msg, e)
        import sys
        sys.print_exception(e)

  async def handle_event(self, name, data):
    print('heater produced event', name, data)
    if name == 'temp':
      await self.mqtt.publish(self.temp_topic, str(data))
    elif name == 'target_temp':
      await self.mqtt.publish(self.target_temp_topic, str(data))
    elif name == 'state':
      await self.mqtt.publish(self.mode_topic, str(data))
    else:
      print('something changed on a heater', name, data)

    # self.mqtt.publish(self.mode_topic, 'OFF')
