# RabbitMQ Chat
Este é um projeto de estudos de mensageria que tem como objetivo desenvolver canais de chat utilizando a tecnologia de mensageria RabbitMQ. 

![image](https://user-images.githubusercontent.com/42682736/239781889-88dbc398-b86c-45af-87ef-564697c09812.png)

## Configurações 
Crie na raiz do projeto o arquivo `.env` e introduza nele as informações necessárias a conexão com o servidor do rabbitMQ, caso use as informações padrão ficará assim:

```env
# RabbitMQ
RABBITMQ_HOST=
RABBITMQ_PORT=
RABBITMQ_USERNAME=
RABBITMQ_PASSWORD=

# Database
DATABASE_NAME=
```

## Execução
1. Executar `pip install -r requirements.txt` para instalar os requisitos na sua máquina
2. Rode o arquivo `api.py` para a api começar a rodar.
3. Em outro terminal rode o arquivo `client.py` para iniciar o client.

