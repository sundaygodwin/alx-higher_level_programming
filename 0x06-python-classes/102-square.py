#!/usr/bin/python3

class Square:
    """A class to represent a square."""

    def __init__(self, size=0):
        """
        Constructor for the Square class.

        Args:
            size (int): Length of a side of the square.
        """
        self.__size = size

    @property
    def size(self):
        """
        Property for the size, representing the length of a side of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size * self.__size

    def __le__(self, other):
        """Check if the area of this square is less than or equal to another square's area."""
        return self.area() <= other.area()

    def __lt__(self, other):
        """Check if the area of this square is less than another square's area."""
        return self.area() < other.area()

    def __ge__(self, other):
        """Check if the area of this square is greater than or equal to another square's area."""
        return self.area() >= other.area()

    def __ne__(self, other):
        """Check if the area of this square is not equal to another square's area."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Check if the area of this square is greater than another square's area."""
        return self.area() > other.area()

    def __eq__(self, other):
        """Check if the area of this square is equal to another square's area."""
        return self.area() == other.area()
