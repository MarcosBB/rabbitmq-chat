import json
from datetime import datetime

class TopicClient:
    def __init__(self, username, queue_name, routing_key, channel):
        self.username = username
        self.queue_name = queue_name
        self.routing_key = routing_key
        self.channel = channel

    def send_message(self, message):
        self.channel.basic_publish(
            exchange="groups", 
            routing_key=self.routing_key, 
            body=self.__get_json_payload(message),
        )

    def __parse_message__(self, body:dict):
        user = body['username']
        message = body['message']
        timestamp = body['timestamp']
        return f"{user} [{timestamp[11:]}]: {message}"

    def __get_json_payload(self, message):
        return json.dumps({
            "username": self.username,
            "message": message,
            "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })

    def receive_message(self):
        def callback(ch, method, properties, body):
            print(f"Mensagem recebida: {body}")

        self.channel.basic_consume(
            queue=self.queue_name, 
            on_message_callback=callback, 
            auto_ack=True
        )
        self.channel.start_consuming()

    def get_one_message(self):

        method_frame, header_frame, body = self.channel.basic_get(self.queue_name)
        if method_frame:
            self.channel.basic_ack(method_frame.delivery_tag)
            bodydict = json.loads(body)
            msg = self.__parse_message__(bodydict)
            return msg
        else:
            return ''