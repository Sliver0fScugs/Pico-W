import time
from machine import Pin # type: ignore

pir = Pin(16, Pin.IN, Pin.PULL_DOWN)
buzzer = Pin(7, Pin.OUT)
led1 = Pin(2, Pin.OUT)
led2 = Pin(3, Pin.OUT)
led3 = Pin(4, Pin.OUT)
led4 = Pin(5, Pin.OUT)
led5 = Pin(6, Pin.OUT)
readyled = Pin(0, Pin.OUT)

leds = [led1, led2, led3, led4, led5]

activeleds = 0
counting = False
count = 0

ready = True

for led in leds:
    led.off()
    

def FourFlash():
    for i in range(4):
        for led in leds:
            led.off()
        buzzer.on()
        time.sleep(0.07)
        buzzer.off()
        time.sleep(0.1)
        for led in leds:
            led.on()
        time.sleep(0.1)
        buzzer.on()
        time.sleep(0.07)
        buzzer.off()
    for led in leds:
        led.off()

e = 1

while True:
    #if pir.value() == 1 and counting == False:
    if e == 1 and counting == False:
        activeleds += 1
        counting = True
        ready = False
    if activeleds >= 1:
        led1.on()
    if activeleds >= 2:
        led2.on()
    if activeleds >= 3:
        led3.on()
    if activeleds >= 4:
        led4.on()
    if pir.value() == 0 and ready == False:
        ready = True

    if activeleds >= 5:
        FourFlash()
        activeleds = 0

    if counting == True:
        count += 1
        readyled.off()
    if count == 30000:
        count = 0
        counting = False
    if counting == False:
        readyled.on()
    
    