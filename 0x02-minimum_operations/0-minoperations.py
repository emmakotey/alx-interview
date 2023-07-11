#!/usr/bin/python3
"""
This module provides a function to calculate the fewest number of operations needed to result in exactly n H characters in a file.
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in a file.
    """
    if n <= 1:
        return 0

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i + minOperations(n // i)

    return n


if __name__ == "__main__":
    n = 9
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))
