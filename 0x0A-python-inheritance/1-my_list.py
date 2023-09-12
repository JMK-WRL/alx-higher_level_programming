#1/usr/bin/python3
"""class defines mylist"""

class MyList(list):
    def print_sorted(self):
        """Print the list in asceding order that is sorted"""

        sorted_list = sorted(self)
        print(sorted_list)