# main.py -- put your code here!

import pycom
import time
from machine import Pin

p9 = Pin('P9', mode=Pin.OUT)
p10 = Pin('P10', mode=Pin.OUT)
p11 = Pin('P11', mode=Pin.OUT)


pycom.heartbeat(False)
while True:
   pycom.rgbled(0x007f00)
   time.sleep(1)
   pycom.rgbled(0x7f7f00)
   time.sleep(1)
   pycom.rgbled(0x7f0000)
   time.sleep(1)

