from machine import Pin, ADC, DAC
import time

from mqtt import MQTTClient
from network import WLAN
import machine

###########################################
#                 ADC DAC
###########################################
adc = ADC()
p_input = adc.channel(pin="P14", attn=ADC.ATTN_11DB) # analog input
p_output = DAC("P22")                                # analog output

# while True:
#     time.sleep(.3)
#     print(p_input() / 4095)
#     p_output.write(p_input() / 4095)


###################################
#
###################################
# ต่อ wifi
wlan = WLAN(mode=WLAN.STA)
nets = wlan.scan()
for net in nets:
    print(net)
    if net.ssid == 'code':
        print('[wifi] found....')
        wlan.connect(net.ssid, auth=(net.sec, '81555084'), timeout=10000)
        while not wlan.isconnected():
            machine.idle()
        print('[wifi] connected..!!')
        break


def sub_cb(topic, msg):
    print(msg)

client = MQTTClient("59070174", "broker.mqttdashboard.com")
client.set_callback(sub_cb)
client.connect()
client.subscribe(topic="kmitl")

while True:
    print(p_input() / 4095)
    p_output.write(p_input() / 4095) # analog output
    client.publish(topic="kmitl", msg="%f" % (p_input() / 4095))
    time.sleep(1)
