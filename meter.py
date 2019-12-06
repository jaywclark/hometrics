import gpiozero
from signal import pause

from telegraf.client import TelegrafClient
client = TelegrafClient(host='10.10.10.42', port=8092)


led = gpiozero.LED(17)
counter = gpiozero.Button(2)

def gallon_pulse_on():
    led.on()
    client.metric('pulse', 1, tags={'meter': 'outside'})

def gallon_pulse_off():
    led.off()

counter.when_pressed = gallon_pulse_on
counter.when_released = gallon_pulse_off

pause()