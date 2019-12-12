from signal import pause
from pulse import pulse_count
import threading
import time


class main(object):
    def __init__(self, interval=1):

        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            # Do something
            print('Do something here later',flush=True)

            time.sleep(self.interval)

class pulse(object):
    def __init__(self):
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = False
        time.sleep(5)
        thread.start()

    def run(self):
        print('Initializing pulse inputs',flush=True)
        pulse_count()

print('starting hometrics',flush=True)

main()
pulse()

