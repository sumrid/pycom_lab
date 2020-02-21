# pylint: disable=maybe-no-member
# main.py -- put your code here!

import pycom
import time
from machine import Pin  # เป็น lib ของบอร์ด ขึ้นอยู่กับรุ่นของบอร์ด

p9 = Pin('P9', mode=Pin.OUT)
p10 = Pin('P10', mode=Pin.OUT)
p11 = Pin('P11', mode=Pin.OUT)


def changeRGB(pin9, pin10, pin11):
    p9.value(pin9)
    p10.value(pin10)
    p11.value(pin11)


pycom.heartbeat(False) # ปิดไฟกระพริบ
while True:
    pycom.rgbled(0x007f00) # green
    changeRGB(0, 1, 1)
    time.sleep(1)

    pycom.rgbled(0x7f7f00) # yellow
    changeRGB(1, 0, 1)
    time.sleep(1)

    pycom.rgbled(0x7f0000) # red
    changeRGB(1, 1, 0)
    time.sleep(1)

    changeRGB(0, 0, 1)
    time.sleep(1)

    changeRGB(1, 0, 0)
    time.sleep(1)

    changeRGB(0, 1, 0)
    time.sleep(1)

    changeRGB(0, 0, 0)
    time.sleep(1)
