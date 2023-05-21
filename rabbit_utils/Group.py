class Group:
    def __init__(self, name, channel):
        self.name = name
        self.channel = channel
        self.group_name = name
        self.routing_key = f"group.{name.replace(' ', '_')}"
        self.exchange = self.channel.exchange_declare(
            exchange="groups", 
            exchange_type='topic'
        )
        
    def create_queue(self, username):
        queue_name = f"{self.routing_key}.{username}"

        self.channel.queue_declare(queue=queue_name)
        self.channel.queue_bind(
            exchange="groups", 
            queue=queue_name, 
            routing_key=self.routing_key,
        )

        return queue_name
    