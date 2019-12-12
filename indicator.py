
import gpiozero
import time

def blink(indicatorled = gpiozero.LED(17)):
    indicatorled.blink(n=1,background=True)
