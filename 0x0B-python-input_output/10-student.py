#!/usr/bin/python3
"""Contains a class student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Student class initialization.

        Args:
            first_name: student's first name.
            last_name: studnet's last name.
            age: student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dict representation of a Student instance.
        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved.
        """
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        else:
            return self.__dict__
