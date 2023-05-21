import os
import pika
import signal
import sys

class RabbitHandler:
    def __init__(self):
        self.connection = self.__create_connection()
        self.channel = self.connection.channel()
        self.__prevents_unexpected_closures()
        
    def __create_connection(self):
        connection_parameters = pika.ConnectionParameters(
            host=os.getenv("RABBITMQ_HOST"),
            port=os.getenv("RABBITMQ_PORT"),
            credentials=pika.PlainCredentials(
                username=os.getenv("RABBITMQ_USERNAME"),
                password=os.getenv("RABBITMQ_PASSWORD"),
            )
        )
        return pika.BlockingConnection(connection_parameters)
    
    def close_connection(self):
        self.connection.close()

    def __prevents_unexpected_closures(self):
        def signal_handler(signal, frame):
            self.close_connection()
            sys.exit(0)

        signal.signal(signal.SIGINT, signal_handler)
        sys.exitfunc = self.close_connection
