#!/usr/bin/python3
"""Defines rectangle class."""


class Rectangle:
    """Represent rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the printable representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join([str(self.print_symbol) * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Return a string representation of the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the bigger rectangle based on area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Create a new Rectangle instance with equal width and height."""
        return cls(size, size)

