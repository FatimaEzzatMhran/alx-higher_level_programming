#!/usr/bin/python3
"""
This script contains the class definition of a City
and an instance Base = declarative_base().
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
    """
    City class has the following attributes:
    __tablename__: the table name of the class
    id: The state id of class City - 
        Integer, auto-generated, unique, not nullable
    name: The city name of class City -
          String, 128, not nullable
    state_id: The state id -
              Integer, foreign key, not nullable
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
