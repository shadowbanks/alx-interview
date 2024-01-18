#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Calculates the fewest number of operations
    needed to result in exactly n H characters
    """
    if n <= 1:
        return 0

    count = 0
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            count += divisor
            n //= divisor
        divisor += 1

    if n > 1:
        count += n

    return count
