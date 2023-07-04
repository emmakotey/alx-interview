#!/usr/bin/python3
"""Defines a function that determines if a box containing a list
   of lists can be opened using keys stored in the lists
"""

def canUnlockAll(boxes):
    n = len(boxes)
    keys = set(boxes[0])
    visited = set([0])
    queue = [0]

    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if key not in visited:
                visited.add(key)
                keys.add(key)
                queue.append(key)

        if len(visited) == n:
            return True

    return False