#!/usr/bin/python3
"""
This script contains the class definition of a State
and an instance Base = declarative_base().
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class has the following attributes:
    __tablename__: the table name of the class
    id: The state id of class state - Integer
    name: The state name of class state - String
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
