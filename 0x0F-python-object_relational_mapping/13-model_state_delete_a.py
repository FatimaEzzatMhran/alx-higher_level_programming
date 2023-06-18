#!/usr/bin/python3
"""
This script deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
"""


import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    """Access to the db to get the states"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    """Create a session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """Query the database to retrieve all State objects that contains a"""
    states_to_delete = session.query(State).filter(State.name.contains('a'))

    """Deletes the states that contains letter a -if found-"""
    if states_to_delete is not None:
        for state in states_to_delete:
            session.delete(state)

    session.commit()
