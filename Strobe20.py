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
led9 = Pin(7, Pin.OUT)
led10 = Pin(6, Pin.OUT)
led11 = Pin(5, Pin.OUT)
led12 = Pin(4, Pin.OUT)
led13 = Pin(3, Pin.OUT)
led14 = Pin(2, Pin.OUT)
led15 = Pin(1, Pin.OUT)
led16 = Pin(0, Pin.OUT)
led17 = Pin(16, Pin.OUT)
led18 = Pin(17, Pin.OUT)
led19 = Pin(18, Pin.OUT)
led20 = Pin(19, Pin.OUT)


leds = [led1, led2, led3, led4, led5, led6, led7, led8, led9, led10, led11, led12, led13, led14, led15, led16, led17, led18, led19, led20]

firstTime = True

SleepTime = 0.5

while True:
    for i in range(20):
        leds[i].on()
        if i != 0:
            leds[i - 1].off()
        else:
            leds[19].off()
        utime.sleep(SleepTime)
        if SleepTime < 0.005:
            SleepTime = 1.0
        SleepTime = SleepTime / 1.03
    
        