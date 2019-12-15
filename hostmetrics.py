import psutil
from telegrafsend import sendmetric
from config import conf
import threading

class load(object):
    def __init__(self):
        self.cpu=psutil.cpu_percent()
        self.mem=psutil.virtual_memory()[2]
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = False
        thread.start()

    def run(self):
        sendmetric('cpu_percent_used', self.cpu, {'piname': conf['pi']['piname']})
        sendmetric('mem_percent_used', self.mem, {'piname': conf['pi']['piname']})
