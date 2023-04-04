#!/usr/bin/python3
"""
This is text indentation module.

It has one function that takes one required parameter.
"""


def text_indentation(text):
    """Print text with two new lines after each '.', '?' and ':'.

    Args:
        text (string): Text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = 0
    for i in text:
        if flag == 0:
            if i == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if i == '?' or i == '.' or i == ':':
                print(i)
                print()
                flag = 0
            else:
                print(i, end="")
