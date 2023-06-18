#!/usr/bin/python3
"""
This script adds the State object “Louisiana”
to the database hbtn_0e_6_usa
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

    """Add the State object -Louisiana- """
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    """Print the new_state id"""
    print(new_state.id)
