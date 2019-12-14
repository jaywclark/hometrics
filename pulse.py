import gpiozero
from telegrafsend import sendmetric
from indicator import blink
from signal import pause
from config import conf


def record_count(btn,indicatorled = gpiozero.LED(17)):
    sendmetric('pulse', 1, {'id':conf['pulse'][str(btn.pin)]['pin'], 'metername': conf['pulse'][str(btn.pin)]['metername'], 'utility': conf['pulse'][str(btn.pin)]['utility']})
    blink(indicatorled)


def pulse_count():
    
    counters={}
    for x in conf['pulse']:
        counters[x]=gpiozero.Button(x, hold_time=.1)
        counters[x].when_held = record_count
    pause()