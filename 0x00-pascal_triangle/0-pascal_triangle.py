#!/usr/bin/python3
"""
Pascal Triangle
"""


def pascal_triangle(n):
    """
    Create a pascal triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]

    if n > 1:
        triangle.append([1, 1])

        for i in range(1, n - 1):
            arr = [1]
            for j in range(len(triangle[i]) - 1):
                arr.append(triangle[i][j] + triangle[i][j + 1])
            arr.append(1)
            triangle.append(arr)

    return triangle
