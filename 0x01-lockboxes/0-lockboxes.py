#!/usr/bin/python3
"""
Define a function that determines whether
all boxes provided can be opened.
"""


def canUnlockAll(boxes):
    """
    Determine whether `boxes` can be opened.

    Parameters
        boxes : list
        A list of list containing numbers.

    Returns:
        True if all boxes can be opend
        otherwise False.
    """
    opened_boxes = {0}

    fetch_keys(boxes, boxes[0], opened_boxes)

    return (len(opened_boxes) == len(boxes))


def fetch_keys(boxes, box, opened_boxes):
    """
    Fetch the next key from a box.

    Parameters
        boxes : list
        A list of lists containing the supposed
        keys to boxes.

        box : list
        A box from which a key can be retrieved.
        This will always be the current box.

        opened_boxes : set
        A set storing the keys found in consecutive
        boxes.
    """
    if (not box):
        return

    for index in range(0, len(box)):
        if (box[index] >= len(boxes) or
                box[index] in opened_boxes):
            return

        opened_boxes.add(box[index])
        fetch_keys(boxes, boxes[box[index]], opened_boxes)
