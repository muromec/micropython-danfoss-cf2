import machine

machine_id = machine.unique_id()[0]
machine_id |= machine.unique_id()[1] << 8
machine_id |= machine.unique_id()[2] << 16
machine_id |= machine.unique_id()[3] << 24

mqtt_client = 'sensor/{}'.format(machine_id)

#mqtt_host = '192.168.1.1'
#mqtt_port = 8883
mqtt_user = 'something'
mqtt_secret = 'something'
mqtt_config = (mqtt_client, mqtt_host, mqtt_port, mqtt_user, mqtt_secret, 600)

wifi_network = 'ssid'
wifi_password = 'password'
