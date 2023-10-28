#!/usr/bin/python3

import math

class MagicClass:
    """
    A class representing a Magic Circle.

    Attributes:
        __radius (float): The radius of the magic circle.
    """

    def __init__(self, radius=0):
        """
        Initialize a MagicClass instance with a given radius.

        Args:
            radius (int or float): The radius of the magic circle.
        Raises:
            TypeError: If the radius is not a number (int or float).
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = float(radius)

    def area(self):
        """
        Calculate and return the area of the magic circle.

        Returns:
            float: The area of the magic circle.
        """
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        """
        Calculate and return the circumference of the magic circle.

        Returns:
            float: The circumference of the magic circle.
        """
        return 2 * math.pi * self.__radius
