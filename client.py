import json
from rabbit_utils import RabbitHandler
from dotenv import load_dotenv
from rabbit_utils import Group, RabbitHandler

load_dotenv()

class ClientChat:
    def __init__(self, username, queue_name, routing_key, channel):
        self.username = username
        self.queue_name = queue_name
        self.routing_key = routing_key
        self.channel = channel

    def send_message(self, message):
        self.channel.basic_publish(
            exchange="groups", 
            routing_key=self.routing_key, 
            body=self.__get_json_payload(message),
        )

    def __get_json_payload(self, message):
        return json.dumps({
            "username": self.username,
            "message": message,
        })

    def receive_message(self):
        def callback(ch, method, properties, body):
            print(f"Mensagem recebida: {body}")

        self.channel.basic_consume(
            queue=self.queue_name, 
            on_message_callback=callback, 
            auto_ack=True
        )
        self.channel.start_consuming()


# username = input("Digite seu nome de usuário: ")
username = "joao"

# recebe lista de groupos que pode se inscrever
exchange_name = "groups"
routing_key = "group.adoradores_de_carros"

# se inscreve em um grupo
queue_name = "group.adoradores_de_carros.joao"

# loop de envio e recebimento de mensagens
server = RabbitHandler()
channel = server.channel

chat = ClientChat(username, queue_name, routing_key, channel)
chat.receive_message()

# while True:
#     message = input("Digite sua mensagem: ")
#     chat.send_message(message)

