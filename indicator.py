
import gpiozero
import time

def blink(indicatorled):
    indicatorled.blink(on_time=.2,n=1,background=True,)
