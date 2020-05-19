#! python 3
# strong_password.py - Detects whether a password is strong enough and provides
# a detailed message stating what is missing.

import re

password = str(input("Please enter a password: "))

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
