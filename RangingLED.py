import utime
from machine import Pin, ADC

pot = ADC(Pin(26))
led = Pin(15, Pin.OUT)

while True:
    pot_value = pot.read_u16()
    led.value(pot_value)
    print(pot_value)

