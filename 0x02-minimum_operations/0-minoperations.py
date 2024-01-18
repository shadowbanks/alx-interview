#!/usr/bin/python3
"""
Minimum Operations
"""


def is_prime(n):
    """Check if a number is a prime number"""

    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def largestPrimeDiv(num):
    """Find largest prime divisor"""

    if num <= 1:
        return None

    for i in range(int(num**0.5), 1, -1):
        if num % i == 0 and is_prime(i):
            return i
    return num


def minOperations(n):
    """
    calculates the fewest number of operations
    needed to result in exactly n H characters
    """

    primeDiv = largestPrimeDiv(n)

    if primeDiv is None:
        return 0

    if primeDiv == n:
        return n

    return int(primeDiv + (n / primeDiv))
