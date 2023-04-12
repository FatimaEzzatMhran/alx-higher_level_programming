#!/usr/bin/python3
"""adds all arguments to a Python list and then saves them to a file."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
                    __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"

    try:
        items_list = load_from_json_file(filename)
    except FileNotFoundError:
        items_list = []
    items_list.extend(sys.argv[1:])
    save_to_json_file(items_list, filename)
