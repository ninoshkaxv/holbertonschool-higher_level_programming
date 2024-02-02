#!/usr/bin/python3
"""This module define a square

"""


class Square():
    """ Define  square

    Args:
        size: the size of the square
    """
    def __init__(self, size=0):
        self.__size = int(size)

    def area(self):
        """Method that return the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """Get the size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = int(value)
