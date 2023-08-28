#!/usr/bin/python3

def safe_print_list_integer(my_list=[], x=0):
    try:
        count = 0
        for item in my_list:
            if count < x:
                if type(item) is int:
                    print("{:d}".format(item), end=' ')
                    count += 1
            else:
                break
            print()
            return count
    except Exception:
        return count
