# !/usr/bin/python3
# comma_code.py - Takes in a list object and returns a string with all items
# separated by a comma and a space, and with "and" inserted before the final
# item.

LIST_OBJ = ['apples', 'bananas', 'tofu', 'cats']

def comma_code(LIST_OBJ):
    LIST_OBJ.insert(-1, 'and')
    new_str = ', '.join(LIST_OBJ[:-2]) + ", and " + LIST_OBJ[-1]
    return new_str

comma_code(LIST_OBJ)
