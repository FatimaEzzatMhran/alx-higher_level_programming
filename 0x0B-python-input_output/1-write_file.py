#!/ust/bin/python3
"""Contains one function called the write_file function."""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8).

    Args:
        file_name: name of the file to write to.
        text: the text that will be written to the file.
    Returns:
        The number of chars writtem.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
