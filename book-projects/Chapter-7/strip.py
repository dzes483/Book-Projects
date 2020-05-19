#! python3
# strip.py - A function version of the strip() string method. It can replace
# the spaces with a character or characters of the user's choice.

import re

strip_left = re.compile(r'^\s*')    # all space characters to the left
strip_right = re.compile(r'\s*$')   # all space characters to the right
strip = re.compile(r'^\s*|\s*$')


def strip_func(str, char=None):
    if not char:        # if no character is specified, just strip the string
        # new_str = re.sub(strip_left, "", str)
        # new_str = re.sub(strip_right, "", new_str)
        new_str = re.sub(strip, "", str)
        return new_str
    else:               # otherwise, replace the whitespace with the character
        new_str = re.sub(r'^\s*|\s*$', char, str)
        return new_str

strip_func('   Hello there fellow!   ')
