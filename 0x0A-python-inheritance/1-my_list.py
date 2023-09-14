#!/usr/bin/python3
"""Function prints the lists inherited
"""


class MyList(list):
    """child class of list
    """
    def print_sorted(self):
        """
        Module to sort a list
        """
        print(sorted(self.copy()))
        """
        => This is another solution for:
        new_list = list.copy(self)
        list.sort(new_list)
        print(new_list)
        """