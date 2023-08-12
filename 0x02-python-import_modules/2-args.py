#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("0 arguments")
        print(".")
    else:
        print("arguments {}:".format(num_args))

        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
        print()
