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
    # Start by assuming the codepoint contains
    # only 1 chunk
    chunk = 1

    for item in data:
        if (chunk == 1):
            # Determine the number of chunks
            if (item >> 5 == 0b110 or item >> 5 == 0b1110):
                chunk = 2
            elif (item >> 4 == 0b1110):
                chunk = 3
            elif (item >> 3 == 0b11110):
                chunk = 4
            elif (item >> 7 & 0b1):
                return (False)
        else:
            # Check if continuation bytes of
            # the multi-byte chunk is valid
            if (item >> 6 != 0b10):
                return (False)

            # Ensure the next continuation
            # byte is checked
            chunk -= 1

    return (chunk == 1)
