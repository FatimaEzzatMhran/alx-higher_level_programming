#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa
"""


import sys
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Access to the db to get the states"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    """Create a session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """Query the database to retrieve all City objects"""
    results = session.query(City, State)\
        .filter(State.id == City.state_id)\
        .order_by(City.id.asc())

    """Print the results"""
    for city, state in results.all():
        print(f"{state.name}: ({city.id}) {city.name}")
