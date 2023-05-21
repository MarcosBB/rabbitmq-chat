from rabbit_utils import RabbitHandler
from dotenv import load_dotenv
from rabbit_utils import RabbitHandler, ClientChat

load_dotenv()


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
messages = []
while True:
    msg = chat.get_one_message()
    if msg != '':
        messages.append(msg)
    print("mensagens recebidas:\n")
    for msg in messages:
        print(msg)
    message = input("Digite sua mensagem: ")
    if message == '': break
    chat.send_message(message)
