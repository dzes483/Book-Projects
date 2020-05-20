#!/usr/bin/python3
# strong_password.py - Detects whether a password is strong enough. It does not
# provide a detailed error message as to why it is not strong.

import re

password = str(input("Please enter a password: "))

strong_pword_regex = re.compile(r'''
                                ^(?=.*?\d)      # At least one digit
                                (?=.*?[A-Z])    # At least one uppercase letter
                                (?=.*?[a-z])    # At least one lowercase letter
                                [A-Za-z\d]{8,}$ # At least 8 characters long
                                ''', re.VERBOSE)
try:
    strong_true = strong_pword_regex.search(password).group()
except AttributeError:
    print('Your password is not strong!')
else:
    print('Your password is strong!')
