#!/usr/bin/python3
# strip.py - A function version of the strip() string method. It can replace
# the spaces with a character or characters of the user's choice.

import re

strip = re.compile(r'^\s*|\s*$')


def strip_func(str, char=None):
    if not char:        # if no character is specified, just strip the string
        new_str = re.sub(strip, "", str)
        return new_str
    else:               # otherwise, replace the whitespace with the character
        new_str = re.sub(strip, char, str)
        return new_str

str = input("Enter the string you'd like to strip: ")
char = input("Enter the character you'd like to replace the whitespace with \
            (if desired). If not, press 'ENTER'.")

strip_func(str, char)
