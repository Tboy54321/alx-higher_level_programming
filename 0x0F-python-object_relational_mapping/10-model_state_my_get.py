#!/usr/bin/python3
'''
Script that prints the first state from the database
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy.exc import NoResultFound
import sys


def get_state(username, password, database_name, search_name):
    engine = create_engine(f'mysql://{username}:\
            {password}@localhost:3306/{database_name}')

    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).filter(State.name == search_name).first()
    if state is not None:
        print('{0}'.format(state.id))
    else:
        print("Not found")

    '''
    try:
        state = session.query(State).filter(State.name == search_name).first()
        print(state.id)
    except NoResultFound:
        print("Not found")
    '''

    session.close()


if __name__ == "__main__":
    from model_state import Base, State

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    search_name = sys.argv[4]

    get_state(username, password, database_name, search_name)
