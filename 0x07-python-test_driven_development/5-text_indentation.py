#!/usr/bin/python3
# 5-text_indentation


def text_indentation(text):
    """
    prints a text with 2 new lines after '.', '?' and ':' characters

    Args:
        text (str): the input text
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for char in text:
        print(char, end='')

        if char in ['.', '?', ':']:
            print("\n\n", end='')