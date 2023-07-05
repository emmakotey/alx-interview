#!/usr/bin/python3
"""This function accertains if a box containing a list
   can be opened using keys stored in those lists
"""


def canUnlockAll(boxes):
    """Determines if boxes can be unlocked"""
    position = 0
    unlocked = {}

    for box in boxes:
        if len(box) == 0 or position == 0:
            unlocked[position] = "always_unlocked"
        for key in box:
            if key < len(boxes) and key != position:
                unlocked[key] = key
        if len(unlocked) == len(boxes):
            return True
        position += 1
    return False
