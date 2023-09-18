#!/usr/bin/python3
'''
Script that prints the first state from the database
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def print_first_state(username, password, database_name):
    engine = create_engine(f'mysql://{username}:\
            {password}@localhost:3306/{database_name}')

    Session = sessionmaker(bind=engine)

    session = Session()

    new_state = State(name="Louisiana")

    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()


if __name__ == "__main__":
    from model_state import Base, State

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    print_first_state(username, password, database_name)
