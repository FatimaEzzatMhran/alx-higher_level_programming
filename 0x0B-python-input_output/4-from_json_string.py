#!/usr/bin/python3
"""Contains one function called from_json_string."""
import json


def from_json_string(my_str):
    """returns an object represented by JSON string."""
    return (json.loads(my_str))
