#!/usr/bin/python3
"""
changes the name of a State object from the database hbtn_0e_6_usa
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

    """Query the database to update the state where id=2 to -New Mexico-"""
    state = session.query(State).filter(State.id == 2).first()

    """Update the name of the object"""
    state.name = "New Mexico"
    session.commit()
