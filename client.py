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

# Não recebe mensagens ao mesmo tempo que envia
# Para testar comente a linha abaixo e descomente o while True e vice-versa
# chat.receive_message()
while True:
    message = input("Digite sua mensagem: ")
    chat.send_message(message)

