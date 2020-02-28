
from machine import ADC, DAC
import time

from mqtt import MQTTClient
from network import WLAN
import machine

###################################
#             ADC DAC
###################################
adc = ADC()
p_input = adc.channel(pin="P14", attn=ADC.ATTN_11DB) # analog input
p_output = DAC("P22")                                # analog output

###################################
#              MQTT
###################################
# ต่อ wifi
wlan = WLAN(mode=WLAN.STA)
nets = wlan.scan()

for net in nets:
    print(net)
    if net.ssid == '@305':                 # <<< ชื่อ wifi 
        print('[wifi] found....%s' % net.ssid)
        wlan.connect(net.ssid, auth=(net.sec, '0892322022'), timeout=10000)
        while not wlan.isconnected():
            machine.idle()
        print('[wifi] connected..!!')
        break


# subscribe and publish to MQTT
def sub_cb(topic, msg): # callback เพื่อบอกว่าเวลาได้ค่ามา ให้ทำอะไรต่อ
    print(msg)

client = MQTTClient("59070174", "broker.mqttdashboard.com")
client.set_callback(sub_cb)
client.connect()
client.subscribe(topic="kmitl/one")

while True:
    # print(p_input() / 4095)
    p_output.write(p_input() / 4095) # analog output
    client.publish(topic="kmitl", msg="%f" % (p_input() / 4095))
    time.sleep(1)

