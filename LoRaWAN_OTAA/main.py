from network import LoRa
import socket
import time
import ubinascii  # micropython module
import struct  # for ABP
import pycom
pycom.heartbeat(False)
pycom.rgbled(0xECEB1A)

# create LoRa asia region
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.AS923, device_class=LoRa.CLASS_C)
print('Device EUI:', ubinascii.hexlify(lora.mac()).upper().decode('utf-8'))


################
#     OTAA
################
app_eui = ubinascii.unhexlify('D8DF149D1DA65EF9')
app_key = ubinascii.unhexlify('E8F1B92F79A72A8C2AA8AE182ADF2B35')
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
while not lora.has_joined():
    time.sleep(2.5)
    print('Not yet joined...')
pycom.rgbled(0x27ED00)
print('Joined!')

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
s.setblocking(False)

# uplink
s.send("Hello from Pycom4")

# วนลูปรอรับข้อมูล
while True:
    time.sleep(3)

    data = s.recv(64)    # recive downlink data
    print("Data:", data) # <-- bytes

    if data != b'':
        try:
            hex_val = ubinascii.hexlify(data)
            number = int(hex_val, 16)
            pycom.rgbled(number)          # set RGB LED
        except:
            pycom.rgbled(0xFF0000)

