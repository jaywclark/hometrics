
import gpiozero
import time

def blink(indicatorled):
    indicatorled.blink(n=1,background=True)
