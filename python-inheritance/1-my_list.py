#!/usr/bin/python3


class MyList(list):
    """A custom list class inheriting from the built-in list"""

    def print_sorted(self):
        """Prints the list in sorted (ascending) order"""
        sorted_list = sorted(self)
        print(sorted_list)

