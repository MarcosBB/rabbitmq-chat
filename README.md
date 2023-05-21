# RabbitMQ Chat
Este é um projeto de estudos de mensageria que tem como objetivo desenvolver canais de chat utilizando a tecnologia de mensageria RabbitMQ. 

## Configurações 
Crie na raiz do projeto o arquivo `.env` e introduza nele as informações necessárias a conexão com o servidor do rabbitMQ, caso use as informações padrão ficará assim:

```env
RABBITMQ_HOST=localhost
RABBITMQ_PORT=5672
RABBITMQ_USERNAME=guest
RABBITMQ_PASSWORD=guest
```

## Execução
1. Executar `pip install -r requirements.txt` para instalar os requisitos na sua máquina
2. Rode o arquivo `api.py` para criar o grupo e a fila de mensagens do client.
3. Rodar o arquivo `client.py` para iniciar o client (Lembrando que até agora só da pra fazer uma coisa de cada vez, ler ou receber mensagens).