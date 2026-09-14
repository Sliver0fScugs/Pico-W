import utime, random
from machine import Pin, ADC

led1 = Pin(14, Pin.OUT)
led2 = Pin(15, Pin.OUT)
led3 = Pin(13, Pin.OUT)
led4 = Pin(12, Pin.OUT)
led5 = Pin(11, Pin.OUT)
led6 = Pin(10, Pin.OUT)
led7 = Pin(9, Pin.OUT)

pot = ADC(Pin(26))



leds = [led1, led2, led3, led4, led5, led6, led7]

firstTime = True

SleepTime = 0.5

while True:
    pot_value = pot.read_u16()
    pot_value = int(pot_value / 9362)
    pot_value -= 1
    for led in leds:
        led.off()
    leds[pot_value].on()

    
        