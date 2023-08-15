#!/usr/bin/python3

def not_c(my_string):
    rem = [x for x in my_string if x !='c' and x != 'C']
    return ("".join(rem))
