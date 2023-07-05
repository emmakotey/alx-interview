#!/usr/bin/python3
"""This function is to check if a box, which holds 
    a list comprised of other lists, can be 
    unlocked using the keys stored within those 
    lists
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
