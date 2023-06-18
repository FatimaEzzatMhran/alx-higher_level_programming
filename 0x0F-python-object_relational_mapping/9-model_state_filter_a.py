#!/usr/bin/python3
"""
This script lists all State objects that contain the
letter 'a' from the database hbtn_0e_6_usa
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
    states = session.query(State).filter(State.name.contains('a'))
    .order_by(State.id).all()

    """Print the results"""
    for instance in states:
        print(f"{instance.id}: {instance.name}")
