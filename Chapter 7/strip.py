#! python3
# strip.py - A function version of the strip() string method.
import re

strip_left = re.compile(r'^\s*')
strip_right = re.compile(r'\s*$')
strip = re.compile(r'^\s*|\s*$')

def strip_func(str, char=None):
    if not char:
        new_str = re.sub(strip, "", str)
        return new_str
    else:
        new_str = re.sub(r'^\s*|\s*$', char, str)
        return new_str

strip_func('   Hello there fellow!   ')
