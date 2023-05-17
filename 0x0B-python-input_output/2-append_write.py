#!/usr/bin/python3
"""Contains one function called the append_write function."""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8).

    Args:
        filename: name of the file that we will append to.
        text: the string to append to the file.
    Returns:
        number of chars appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        chars_appended = f.write(text)
        return (chars_appended)
