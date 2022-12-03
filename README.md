# What is it

MQTT adapter for Danfoss CF-MC heating system to add heating zones status to homeassistant

# How to use it

You need micropython-compatible board, like wemos d1 and radio that works on 866.4 MHz.
This project assumes that radio is rfm69.

# What is this radio protocol

See protocol description here https://github.com/muromec/rtl_433/blob/master/src/devices/danfoss_cf.c

# Can I set temperature with this

No. Radio protocol has 4 bytes of MAC which is not figured out yet, so generating messages is possible,
but they are not processed by the main unit. Replaying captured messages works, but there is one bit
sequence counter which makes things very annoying.

# What messages does this react to

When CF-RD sensor tells main unit what current temperature is, message is relayed to MQTT as current temp topic.
When target temp is changed through CF-RD, message is relayed to MQTT as target temp topic.
Those two can be extrapolated to figure that heating is on of off.

Pressing up/down button on room sensor will trigger message /from/ main unit to remind what target temp is, as
room sensors apparently don't have memory to rely on. That message is also relayed to MQTT as target temp.
