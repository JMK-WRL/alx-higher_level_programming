#!/usr/bin/python3
# Function that creates a copy of the string

def remove_char_at(str, n):
    if n < 0:
        return (str)
    return (str[:n] + str[n + 1:])
