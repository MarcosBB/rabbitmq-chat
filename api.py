from flask import Flask, request
from flask_restful import Resource, Api

import os
from dotenv import load_dotenv
from src.rabbit_utils import Group, RabbitHandler
import sqlite3
from src.utils import (
    create_basic_groups,
    group_db_to_dict,
    group_db_to_list,
)

load_dotenv()
app = Flask(__name__)
api = Api(app)
database = f"{os.getenv('DATABASE_NAME')}.db"


class GroupResource(Resource):
    def get(self):
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM groups")
        groups = cursor.fetchall()
        conn.close()

        return group_db_to_list(groups), 200
    
    
class GroupSubscribeResource(Resource):
    def post(self, id):
        username = request.json["username"]
        # import pdb; pdb.set_trace()
        
        server = RabbitHandler()
        channel = server.channel
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        
        cursor.execute(f"SELECT * FROM groups WHERE id = {id}")
        group = cursor.fetchone()
        group = group_db_to_dict(group)

        queue_name = f"group.{group['routing_key']}.{username}"
        
        channel.queue_declare(queue=queue_name)
        channel.queue_bind(
            exchange=group['exchange'], 
            queue=queue_name, 
            routing_key=group['routing_key'],
        )
        conn.close()
        return {"queue": queue_name}, 200


api.add_resource(GroupResource, '/groups/')
api.add_resource(GroupSubscribeResource, '/groups/<int:id>/subscribe/')

if __name__ == '__main__':
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS groups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            exchange VARCHAR(100) NOT NULL,
            routing_key VARCHAR(100) NOT NULL UNIQUE
        )'''
    )
    create_basic_groups(cursor)

    conn.commit()
    conn.close()

    app.run(debug=True)