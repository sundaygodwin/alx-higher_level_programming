#!/usr/bin/python3
"""Program defines an inherited list class MyList."""


class MyList(list):
    """function Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))

