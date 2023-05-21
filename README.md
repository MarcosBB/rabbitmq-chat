# RabbitMQ Chat
Este é um projeto de estudos de mensageria que tem como objetivo desenvolver canais de chat utilizando a tecnologia de mensageria RabbitMQ. 

## Configurações 
Crie na raiz do projeto o arquivo `.env` e introduza nele as seguintes informações sobre o servidor do rabbitMQ:

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
1. Rode o arquivo `api.py` para criar o grupo e a fila de mensagens do client.
2. Rodar o arquivo `client.py` para iniciar o client (Lembrando que até agora só da pra fazer uma coisa de cada vez, ler ou receber mensagens).