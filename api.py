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


api.add_resource(GroupResource, '/groups/')

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