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

    def to_json(self):
        """retrieves a dict representation of a Student instance."""
        return self.__dict__
