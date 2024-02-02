#!/usr/bin/python3
"""This module define a square

"""


class Square():
    """ Define square

    Args:
        size: the size of the square
    """
    def __init__(self, size=0):
        self.__size = int(size)
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
