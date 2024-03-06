#!/usr/bin/python3
""" method that determines if a given data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """ method that determines if a given data set represents a valid UTF-8 encoding"""
    nbytes = 0

    byte1 = 1 << 7
    byte2 = 1 << 6

    for e in data:
        s = 1 << 7
        if nbytes == 0:
            while s & e:
                nbytes += 1
                s = s >> 1
            if nbytes == 0:
                continue
            if nbytes == 1 or nbytes > 4:
                return False
        else:
            if not (e & byte1 and not (e & byte2)):
                return False
        nbytes -= 1
    return nbytes == 0
