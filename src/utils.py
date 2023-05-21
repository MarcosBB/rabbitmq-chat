
from dotenv import load_dotenv
from src.rabbit_utils import Group, RabbitHandler
load_dotenv()

def create_basic_groups( cursor):
    rabbit_handler = RabbitHandler()
    channel = rabbit_handler.channel

    for group_name in ["grupo da familia", "groupo da turma 2", "grupo da empresa"]:
        group = Group(group_name, channel)
        cursor.execute(
            f"""
                INSERT INTO groups (
                    name, 
                    exchange,
                    routing_key
                ) VALUES (
                    '{group.name}', 
                    'groups',
                    '{group.routing_key}'
                )
                ON CONFLICT DO NOTHING
            """
        )
    rabbit_handler.close_connection()


def group_db_to_dict(group):
    return {
        "id": group[0],
        "name": group[1],
        "exchange": group[3],
        "routing_key": group[2],
    }

def group_db_to_list(groups):
    response = []
    for group in groups:
        response.append(group_db_to_dict(group))
    return response
