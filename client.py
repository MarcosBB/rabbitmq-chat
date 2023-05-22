import requests
from src.rabbit_utils import RabbitHandler
from dotenv import load_dotenv
from src.rabbit_utils import RabbitHandler, TopicClient
from src.CliInterface import CliInterface

load_dotenv()

url = "http://localhost:5000"

def load_groups():
    try:
        response = requests.get(f'{url}/groups/')
        if response.status_code == 200:
            body = response.json()
            return body
        else:
            return []
    except Exception as e:
        return []

def parse_groupslist(group_list):
    text_list = [f'id - nome']
    for group in group_list:
        id = group['id']
        name = group['name']
        text_list.append(f'{id:2} - {name}')
    text_list.append('ou [enter] para encerrar')
    return text_list

def load_queue(username, id):
    try:
        post_data = {'username': username}
        response = requests.post(f'{url}/groups/{id}/subscribe/', json=post_data)
        if response.status_code == 200:
            body = response.json()
            return body['queue']
        else:
            return []
    except Exception as e:
        return []

def get_username():
    username = ''
    while username == '':
        username = input('Digite seu nome de usuário: ')
        if username == '':
            print('Nome de usuário inválido!')
    return username

group_list = load_groups()
if len(group_list) == 0:
    print('Erro ao conectar com o servidor de grupos')
    exit(0)

cli_group_list = parse_groupslist(group_list)
username = get_username()

server = RabbitHandler()
channel = server.channel
chat = TopicClient(username, f"group.grupo da familia.{username}", "group.grupo da familia", channel)
cli_chat = CliInterface()

def update_group(clilist):
    if clilist != cli_group_list:
        clilist.clear()
        clilist.extend(cli_group_list)

def send_group(text):
    if text == '':
        #usuário finalizou
        mode_args['mode'] = 'end'
    else:
        for group in group_list:
            if text == str(group['id']):
                queuename = load_queue(username, text)
                if queuename != '':
                    group_name = group['name']
                    mode_args['mode'] = 'chat'
                    chat.queue_name = queuename
                    chat.routing_key = group['routing_key']
                    cli_chat.cli_list.clear()
                    cli_chat.cli_list.append(f'[CHAT] {group_name}')

def update_message(clilist):
    msg = chat.get_one_message()
    if msg != '':
        clilist.append(msg)

def send_message(text):
    if text == '':
        # usuário finalizou
        mode_args['mode'] = 'group'
    else:
        chat.send_message(text)
    
mode_args = {'mode':'group',
             'chat': {'prompt':'Digite sua mensagem', 'update': update_message, 'send': send_message},
             'group': {'prompt':'Digite o id do chat', 'update': update_group, 'send': send_group}}

cli_chat.start_input(mode_args)
