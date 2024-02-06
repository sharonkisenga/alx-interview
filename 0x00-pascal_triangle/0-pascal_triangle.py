#!/usr/bin/python3
"""returns a list of lists of integers representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """make a list of lists of integers
    parameters:
        n [int]:
            the number of rows
    return:
        [list of lists of ints]:
            representing the pascal's triangle"""
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
