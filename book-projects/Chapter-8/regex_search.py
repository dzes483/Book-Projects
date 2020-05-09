#! python3
# regex_search.py - Opens all .txt files in a folder and searches for any line
# that matches a user-supplied regular expression. The results are printed to
# the screen. The possible regex's are: 'phone number', 'ip address', 'email',
# and 'date' (mm/dd/yyyy).

import os, re, sys, glob

# Regular expressions
# Email address regex
email_regex = re.compile(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', re.IGNORECASE)
# Date regex (mm/dd/yyyy format)
date_regex = re.compile(r'^(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.](19|20)\d\d$')
# IP address regex
ip_regex = re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')
# Phone number regex
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')

# Define folder path and open all .txt files in that folder
folder_path = 'C:\\Users\\Jessica\\AppData\\Local\\Programs\\Python\\Python36\\MyPythonScripts'
for filename in glob.glob(os.path.join(folder_path, '*.txt')):
    with open(filename, 'r') as f:
        text = f.read()
# Ask the user what they want to search for
user_regex = str(input("Please enter what you would like to search for: "))
if user_regex == 'phone number':
    matches = re.findall(phone_num_regex, content)
elif user_regex == 'ip address':
    matches = re.findall(ip_regex, content)
elif user_regex == 'email':
    matches = re.findall(email_regex, content)
elif user_regex == 'date':
    matches = re.findall(date_regex, content)
# Print the results to the screen.
print(matches)
