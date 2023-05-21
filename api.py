import sys
from dotenv import load_dotenv
from rabbit_utils import Group, RabbitHandler

load_dotenv()


# Conectar ao servidor RabbitMQ
try:
    server = RabbitHandler()
    channel = server.channel
    print("Conectado ao servidor RABBITMQ com sucesso!")
except Exception as e:
    print("Não foi possível conectar ao servidor RABBITMQ!")
    sys.exit(1)

# Criar grupo
try:
    grupo_sobre_carros = Group("adoradores de carros", channel)
    print(f"Grupo '{grupo_sobre_carros.group_name}' criado com sucesso!")
except Exception as e:
    print("Não foi possível criar o grupo!")
    server.close_connection()
    sys.exit(1)


# Criar fila
try:
    queue_name = grupo_sobre_carros.create_queue("joao")
    queue_name = grupo_sobre_carros.create_queue("jose")
    print(f"fila '{queue_name}' criada com sucesso!")
except Exception as e:
    print("Não foi possível criar a fila!")
    server.close_connection()
    sys.exit(1)


# Fechar conexão com o servidor RabbitMQ
server.close_connection()
print("Conexão com o servidor RABBITMQ fechada com sucesso!")