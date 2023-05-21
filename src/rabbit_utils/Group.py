class Group:
    def __init__(self, name, channel):
        self.name = name
        self.channel = channel
        self.routing_key = f"group.{name.replace(' ', '_')}"
        self.exchange = self.channel.exchange_declare(
            exchange="groups", 
            exchange_type='topic'
        )
