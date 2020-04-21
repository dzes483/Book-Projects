#! python 3
# strong_password.py - Detects whether a password is strong enough.

import re

password = str(input("Please enter a password: "))

strong_pword_regex = re.compile(r'''
                                ^(?=.*?\d)      # Contains at least one digit
                                (?=.*?[A-Z])    # Contains at least one uppercase letter
                                (?=.*?[a-z])    # Contains at least one lowercase letter
                                [A-Za-z\d]{8,}$ # Is at least eight characters long
                                ''', re.VERBOSE)
try:
    strong_true = strong_pword_regex.search(password).group()
except AttributeError:
    print('Your password is not strong!')
else:
    print('Your password is strong!')
# At least eight characters long
password_length_regex = re.compile(r'([\d|\w]){8,}')
# Contains both uppercase and lowercase characters
password_ucase_regex = re.compile(r'([A-Z]+)')
password_lcase_regex = re.compile(r'([a-z])+')
# Has at least one digit
password_number_regex = re.compile(r'[0-9]+')

try:
    length_true = password_length_regex.search(password).group()
except AttributeError:
    print('Password is not at least eight characters')

try:
    u_case = password_ucase_regex.search(password).group()
except AttributeError:
    print('Password does not have at least one uppercase character.')

try:
    l_case = password_lcase_regex.search(password).group()
except AttributeError:
    print('Password does not have at least one lowercase character.')

try:
    num = password_number_regex.search(password).group()
except AttributeError:
    print('Password does not have at least one number.')

else:
    print('Your password is strong!')
