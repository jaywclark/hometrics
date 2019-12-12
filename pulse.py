import gpiozero
from telegrafsend import sendmetric
from indicator import blink
from signal import pause
from config import conf


def record_count(btn):
    sendmetric('pulse', 1, {'id':conf['pulse'][str(btn.pin)]['pin'], 'metername': conf['pulse'][str(btn.pin)]['metername'], 'utility': conf['pulse'][str(btn.pin)]['utility']})
    blink()


def pulse_count():
    counters={}
    for x in conf['pulse']:
        counters[x]=gpiozero.Button(x)
        counters[x].when_pressed = record_count
    pause()