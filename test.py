import machine
import utime

buzzer = machine.Pin(16, machine.Pin.OUT)

while True:
    buzzer.toggle()
    utime.sleep(0.1)
    buzzer.toggle()
    utime.sleep(0.05)
    buzzer.toggle()
    utime.sleep(0.1)
    buzzer.toggle()
    utime.sleep(0.05)
    buzzer.toggle()
    utime.sleep(0.1)
    buzzer.toggle()
    utime.sleep(0.05)
    buzzer.toggle()
    buzzer.toggle()
    utime.sleep(2)