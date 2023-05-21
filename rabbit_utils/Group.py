class Group:
    def __init__(self, name, channel):
        self.channel = channel
        self.group_name = name
        self.exchange_name = f"group.{name.replace(' ', '_')}"
        self.exchange = self.channel.exchange_declare(
            exchange=self.exchange_name, 
            exchange_type='topic'
        )
        
    def create_queue(self, username):
        queue_name = f"{username}|{self.exchange_name}"
        queue = self.channel.queue_declare(queue=queue_name)
        self.channel.queue_bind(
            exchange=self.exchange_name, 
            queue=queue_name, 
            routing_key=self.group_name
        )

        return queue
    