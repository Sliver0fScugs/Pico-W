import utime, random
from machine import Pin, ADC

led1 = Pin(15, Pin.OUT)
led2 = Pin(14, Pin.OUT)
led3 = Pin(13, Pin.OUT)
led4 = Pin(12, Pin.OUT)
b1 = Pin(11, Pin.OUT)


firstTime = True

SleepTime = 0.5
count = 1

while True:
    if count % 2 == 0:
        led3.off()
        led4.off()
        led1.on()
        led2.on()
        for i in range(300):
            b1.toggle()
            utime.sleep(0.001)
        b1.off()
    else:
        led1.off()
        led2.off()
        led3.on()
        led4.on()
        for i in range(100):
            b1.toggle()
            utime.sleep(0.003)
        b1.off()
    
    
    utime.sleep(0.1)
    count += 1