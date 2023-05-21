from typing import Dict
import pika
import json
from rabbit_utils import RabbitHandler


class Client(RabbitHandler):
    def __init__(self, queue):
        pass


    def send_message(self):
        pass



# recebe lista de groupos que pode se inscrever

# se inscreve em um grupo

# loop de envio e recebimento de mensagens
