import config
import machine
import network
import time


station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(config.wifi_network, config.wifi_password)

while not station.isconnected():
  time.sleep(0.1)
