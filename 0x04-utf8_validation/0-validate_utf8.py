#!/usr/bin/python3
"""
Define a function that validates whether
an input is UTF-8 encoding.
"""


def validUTF8(data):
    """
    Check if the given `data` is a valid
    UTF-8 encoding.

    Parameters:
        data : list
        A list of character encodings
        representing various character sets
        represented as intergers.

    Returns:
        True when `data` contains valid UTF-8
        character sets otherwise False.
    """
    for item in data:
        if (item > 127):
            return (False)

    return (True)
