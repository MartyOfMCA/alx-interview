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
    total_boxes = len(boxes)

    for current_box in range(0, total_boxes):

        keys = boxes[current_box]

        if (not keys and current_box + 1 > max(opened_boxes) and current_box < total_boxes - 1):
            return (False)

        for key in keys:
            if (key < total_boxes):
                opened_boxes.add(key)

    if (len(opened_boxes) == total_boxes):
        return (True)

    return (False)
