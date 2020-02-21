from machine import Pin, ADC, DAC
import time

adc = ADC()

p_input = adc.channel(pin="P14", attn=ADC.ATTN_11DB) # analog input
p_output = DAC("P22")                                # analog output

while True:
    time.sleep(.5)
    print(p_input() / 4095)
    p_output.write(p_input() / 4095)

