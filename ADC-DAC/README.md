## ADC - Analog to Digital Conversion
```python
import machine

adc = machine.ADC()             # create an ADC object
apin = adc.channel(pin='P16')   # create an analog pin on P16
val = apin()                    # read an analog value
```
### adc.channel(* , pin, attn=ADC.ATTN_0DB)
* `pin` ใข้ได้ P13 - P20
* `attn` เป็นการลดค่าแรงดันไฟลง
* ADC pin input range is `0-1.1V.`
* `ถ้าใช้ไฟเข้า 3.3v ควรใช้ attn=ADC.ATTN_11DB`

## DAC
```python
import machine

dac = machine.DAC('P22')        # create a DAC object
dac.write(0.5)                  # set output to 50%

dac_tone = machine.DAC('P21')   # create a DAC object
dac_tone.tone(1000, 0)          # set tone output to 1kHz
```
* dac.write(value) **value ต้องเป็นค่า 0-1**
* แรงดันไฟจะอยู่ที่ 0 - 3.3v