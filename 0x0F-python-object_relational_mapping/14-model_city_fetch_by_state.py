#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa
"""


import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine

if __name__ == "__main__":
    """Access to the db to get the states"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    """Create a session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """Query the database to retrieve all City objects"""
    cities = session.query(State, City).filter(State.id == City.state_id)\
            .order_by(City.id.asc())

    """Print the results"""
    for city, state in cities.all():
        print(f"{state.name}: ({city.id}) {city.name}")
