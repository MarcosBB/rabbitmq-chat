from dotenv import load_dotenv
from rabbit_utils import Group, RabbitHandler
import sys

load_dotenv()


# Conectar ao servidor RabbitMQ
try:
    server = RabbitHandler()
    channel = server.channel
    print("Conectado ao servidor RABBITMQ com sucesso!")
except Exception as e:
    print("Não foi possível conectar ao servidor RABBITMQ!")
    print(e)
    sys.exit(1)


# Criar grupo
grupo_sobre_carros = Group("adoradores de carros", channel)
print(f"Grupo {grupo_sobre_carros.group_name} criado com sucesso!")

queue = grupo_sobre_carros.create_queue("joao")
print("fila criada com sucesso!")


# Fechar conexão com o servidor RabbitMQ
try:
    server.close_connection()
    print("Conexão com o servidor RABBITMQ fechada com sucesso!")
except Exception as e:
    print("Não foi possível fechar a conexão com o servidor RABBITMQ!")
    print(e)
    sys.exit(1)
