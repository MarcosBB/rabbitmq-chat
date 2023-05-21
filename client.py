import json
from rabbit_utils import RabbitHandler
from dotenv import load_dotenv
from rabbit_utils import Group, RabbitHandler

load_dotenv()

class ClientChat:
    def __init__(self, username, queue_name):
        self.queue_name = queue_name
        self.username = username

    def send_message(self, message):
        channel.basic_publish(
            exchange=group_1_name, 
            routing_key=group_1_name, 
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

        channel.basic_consume(
            queue=self.queue_name, 
            on_message_callback=callback, 
            auto_ack=True
        )
        channel.start_consuming()


# username = input("Digite seu nome de usuário: ")
username = "joao"

# recebe lista de groupos que pode se inscrever
group_1_name = "group.adoradores_de_carros"

# se inscreve em um grupo
queue_name = "group.adoradores_de_carros.joao"

# loop de envio e recebimento de mensagens
server = RabbitHandler()
channel = server.channel

chat = ClientChat(username, queue_name)
chat.receive_message()

# while True:
#     message = input("Digite sua mensagem: ")
#     chat.send_message(message)

