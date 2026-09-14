import utime
from machine import Pin, ADC

pir = Pin(16, Pin.IN, Pin.PULL_DOWN)
buzzer = Pin(15, Pin.OUT)
led1 = Pin(14, Pin.OUT)
led2 = Pin(13, Pin.OUT)
led3 = Pin(12, Pin.OUT)
led4 = Pin(11, Pin.OUT)
led5 = Pin(10, Pin.OUT)
readyled = Pin(9, Pin.OUT)

leds = [led1, led2, led3, led4, led5]

activeleds = 0
counting = False
count = 0

ready = True

for led in leds:
    led.off()

while True:
    #if motion detected, active leds += 1, if active leds = 5 then flashing function
    if pir.value() == 1 and counting == False:
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
    if pir.value() == 0:
        ready = True

    if activeleds >= 5:
        for i in range(4):
            for led in leds:
                led.off()
            buzzer.on()
            utime.sleep(0.05)
            buzzer.off()
            utime.sleep(0.1)
            for led in leds:
                led.on()
            utime.sleep(0.1)
            buzzer.on()
            utime.sleep(0.05)
            buzzer.off()
        for led in leds:
            led.off()
        activeleds = 0

    if counting == True:
        count += 1
        readyled.off()
    if count == 20000:
        count = 0
        counting = False
    if counting == False:
        readyled.on()
    
    