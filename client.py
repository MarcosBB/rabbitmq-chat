from rabbit_utils import RabbitHandler
from dotenv import load_dotenv
from rabbit_utils import RabbitHandler, ClientChat
from cli_interface import CliInterface

load_dotenv()


# username = input("Digite seu nome de usuário: ")
username = input('Digite seu nome: ')

# recebe lista de groupos que pode se inscrever
exchange_name = "groups"
routing_key = "group.adoradores_de_carros"

# se inscreve em um grupo
queue_name = f"group.adoradores_de_carros.{username}"

# loop de envio e recebimento de mensagens
server = RabbitHandler()
channel = server.channel
chat = ClientChat(username, queue_name, routing_key, channel)
cli = CliInterface()

def updatemessage(clilist):
    msg = chat.get_one_message()
    if msg != '':
        clilist.append(msg)

cli.start_input("Digite sua mensagem", updatemessage, chat.send_message)
