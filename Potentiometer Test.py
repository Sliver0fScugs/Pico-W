import utime
from machine import Pin, ADC

pot = ADC(Pin(26))
buzzer = Pin(16, Pin.OUT)

buzzerActive = False

while True:
    pot_value = pot.read_u16()
    if pot_value > 30000 and buzzerActive == False:
        buzzer.toggle()
        buzzerActive = True
    if pot_value < 30000 and buzzerActive == True:
        buzzer.toggle()
        buzzerActive = False

