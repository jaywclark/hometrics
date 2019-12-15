from signal import pause
from pulse import pulse_count
import threading
import time
from hostmetrics import load


class main(object):
    def __init__(self, interval=10):

        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()
        pulse()

    def run(self):
        while True:
            load()            
            time.sleep(self.interval)

class pulse(object):
    def __init__(self):
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = False
        thread.start()

    def run(self):
        print('Initializing pulse inputs',flush=True)
        pulse_count()

print('starting hometrics',flush=True)

main()

