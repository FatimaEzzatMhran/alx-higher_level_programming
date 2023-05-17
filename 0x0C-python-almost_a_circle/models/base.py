#!/usr/bin/python3
"""This module contains a class named ``Base``."""
import json


class Base:
    """
    class Base: will be the base of all other classes in this project.
    goal: is to manage id attribute in all future classes.
    why: to avoid duplicating the same code.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization method for Base."""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string."""
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set."""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                list_dict = Base.from_json_string(f.read())
                return [cls.create(**obj) for obj in list_dict]
        except IOError:
            return []
