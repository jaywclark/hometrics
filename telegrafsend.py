from telegraf.client import TelegrafClient
from config import conf

def sendmetric(name, value, tags):
    client = TelegrafClient(host=conf['telegraf']['host'], port=conf['telegraf']['port'])

    print('sending metric', name, tags,flush=True)

    client.metric(name, value, tags=tags)
