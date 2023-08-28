#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            dividend = my_list_1[i] if i < len(my_list_1) else 0
            divisor = my_list_2[i] if i < len(my_list_2) else 0

            if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
                print("Wrong type")
                result.append(0)
            elif divisor == 0:
                print("division by 0")
                result.append(0)
            else:
                result.append(dividend / divisor)
        except IndexError:
            print("out of range")
            result.append(0)

    return result
