#!/usr/bin/python3
"""
This script lists the First State object from the database hbtn_0e_6_usa
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

    """Query the database to retrieve all State objects"""
    first_state = session.query(State).order_by(State.id).first()

    """Print the results"""
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")
