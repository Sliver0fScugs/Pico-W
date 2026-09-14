import utime, random
from machine import Pin, PWM

ybutton = Pin(0, Pin.IN, Pin.PULL_UP)
bled = Pin(1, Pin.OUT)
bbutton = Pin(3, Pin.IN, Pin.PULL_UP)
yled = Pin(2, Pin.OUT)
mr = PWM(Pin(4))
mg = PWM(Pin(5))
mb = PWM(Pin(6))
readyled = Pin(7, Pin.OUT)

bon = False
yon = False


count = 0

bluewin = False
yellowwin = False

bwaiting = 0
ywaiting = 0




def SetColour(r, g, b):
    mr.duty_u16(r)
    mg.duty_u16(g)
    mb.duty_u16(b)


def LightBLights():
    if ybutton.value() == 0:
        yled.on()
        yon = True
    else:
        yled.off()
        yon = False
    if bbutton.value() == 0:
        bled.on()
        bon = True
    else:
        bled.off()
        bon = False



#SetColour(65535, 65535, 0)

count = random.randint(1000, 3000)


while True:
    if count == 0:
        while True:
            LightBLights()
            readyled.on()
            if ybutton.value() == 0 and ywaiting == 0:
                yellowwin = True
                readyled.off()
                break
            if bbutton.value() == 0 and bwaiting == 0:
                bluewin = True
                readyled.off()
                break
        if yellowwin == True:
            SetColour(65535, 65535, 0)
            utime.sleep(3)
            count = random.randint(1000, 3000)
            ywellowwin = False
        if bluewin == True:
            SetColour(0, 0, 65535)
            utime.sleep(3)
            count = random.randint(1000, 3000)
            bluewin = False



    LightBLights()

    if ybutton.value() == 0 and count != 0:
        SetColour(65535, 0, 0)
        ywaiting = 500
    if bbutton.value() == 0 and count != 0:
        SetColour(65535, 0, 0)
        bwaiting = 500

    if count > 0:
        count -= 1
    if ywaiting > 0:
        ywaiting -= 1
    if bwaiting > 0:
        bwaiting -= 1
    utime.sleep(0.01)