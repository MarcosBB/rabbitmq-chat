import os
import pika
import signal
import sys

class RabbitHandler:
    def __init__(self):
        self.__host__ = os.getenv("RABBITMQ_HOST")
        self.__port__ = os.getenv("RABBITMQ_PORT")
        self.__username__ = os.getenv("RABBITMQ_USERNAME")
        self.__password__ = os.getenv("RABBITMQ_PASSWORD")
        self.connection = self.__create_connection()
        self.channel = self.connection.channel()
        
    def __create_connection(self):
        connection_parameters = pika.ConnectionParameters(
            host=self.__host__,
            port=self.__port__,
            credentials=pika.PlainCredentials(
                username=self.__username__,
                password=self.__password__,
            )
        )
        #return CustomConnection(connection_parameters)
        return pika.BlockingConnection(connection_parameters)
    
    def close_connection(self):
        self.connection.close()
