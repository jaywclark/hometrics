
import gpiozero
import time

def blink():
    indicatorled = gpiozero.LED(17)
    indicatorled.on()
    time.sleep(.1)
