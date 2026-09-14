import utime, random
from machine import Pin, ADC

led1 = Pin(14, Pin.OUT)
led2 = Pin(15, Pin.OUT)
led3 = Pin(13, Pin.OUT)
led4 = Pin(12, Pin.OUT)
led5 = Pin(11, Pin.OUT)
led6 = Pin(10, Pin.OUT)
led7 = Pin(9, Pin.OUT)
led8 = Pin(8, Pin.OUT)

leds = [led1, led2, led3, led4, led5, led6, led7, led8]

firstTime = True

SleepTime = 0.5

while True:
    for i in range(8):
        leds[i].on()
        if i != 0:
            leds[i - 1].off()
        else:
            leds[7].off()
        utime.sleep(SleepTime)
        if SleepTime < 0.005:
            SleepTime = 1.0
        SleepTime = SleepTime / 1.2
    
        