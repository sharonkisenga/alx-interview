#!/usr/bin/python3
"""Create a function that returns a list of lists of integers representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """create a list of lists of integers"""
    if type(n) is not int:
        raise TypeError("n is an integer")
    mat = []
    if n <= 0:
        return mat
    for i in range(n):
        arr = []
        for j in range(i+1):
            if j == 0:
                arr.append(1)
            elif j == i:
                arr.append(1)
            else:
                arr.append(mat[i-1][j-1] + mat[i-1][j])
        mat.append(arr)
    return mat
