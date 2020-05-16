from network import LoRa
import socket
import time
import ubinascii # micropython module
import struct # for ABP

# asia region
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.AS923, sf=12)
print('Device EUI:', ubinascii.hexlify(lora.mac()).upper().decode('utf-8'))


##########
#  OTAA
##########
app_eui = ubinascii.unhexlify('70B3D57ED002F1F4')
app_key = ubinascii.unhexlify('D569F48B31D7D92D702662A34C6875B5')
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
while not lora.has_joined():
    time.sleep(2.5)
    print('Not yet joined...')

##########
#  ABP
##########
# dev_addr = struct.unpack(">l", ubinascii.unhexlify('260414D6'))[0]
# nwk_swkey = ubinascii.unhexlify('7E457BB450EC7646C1DCB186832708E4')
# app_swkey = ubinascii.unhexlify('747D1E0CD854092C40EB4B55670E49DD')
# lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))

print("Join success.", lora.has_joined())


s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
s.setblocking(False)
s.send(bytes([0x01, 0x02, 0x03]))
s.settimeout(5.0)

# get any data received (if any...)
data = s.recv(64)
print('received: ', data)
