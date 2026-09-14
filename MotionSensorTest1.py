import utime
from machine import Pin, ADC

pir = Pin(18, Pin.IN, Pin.PULL_DOWN)
buzzer = Pin(16, Pin.OUT)
led = Pin(15, Pin.OUT)

buzzerActive = False

#utime.sleep(3)



while True:
    """
    if pir.value() == 1 and buzzerActive == False:
        buzzer.toggle()    
        buzzerActive = True
    if pir.value() == 0 and buzzerActive == True:
        buzzer.toggle()
        buzzerActive = False
    if pir.value() == 1:
        led.value(1)
    else:
        led.value(0)
    """
    if pir.value() == 1 and buzzerActive == False:
        for i in range(1, 1500):
            led.toggle()
            utime.sleep(1/i)
            led.toggle()
            utime.sleep(1/i)