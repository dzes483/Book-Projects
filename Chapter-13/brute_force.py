#! python3
# brute_force.py - Attempts to decrypt an encrypted PDF file by trying every
# possible English word until it finds one that works.

import PyPDF2
import os
from tqdm import tqdm
import sys

os.chdir('/home/jessica/Documents/Programming/MyPythonScripts')

# Open the dictionary file
word_doc = open('short_dictionary.txt', 'r')

# Read the dictionary file line-by-line
words = word_doc.readlines()

# Open the encrypted PDF
pdf_reader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))

# Create a list of word strings by reading the file and strip whitespace characters
word_list = []
for word in words:
    word_list.append(word.strip().split())

# # TEST
# test_list = ['READY', 'ROCK', 'ROSEBUD', 'ROSEMARY']

def brute_force_func():
    for word in words:
        attempt = pdf_reader.decrypt(word.lower())
        attempt_2 = pdf_reader.decrypt(word.upper())
        if attempt == 1:
            print('Decryption successful. The password was: ' + word.lower())
            success = True
            try:
                sys.exit()
            except SystemExit:
                sys.exit('Decryption successful. Exiting...')
        elif attempt_2 == 1:
            print('Decryption successful. The password was: ' + word.upper())
            success = True
            try:
                sys.exit()
            except SystemExit:
                sys.exit('Decryption successful. Exiting...')
        elif word.lower() == last_word or word.upper() == last_word:
            print('End of list. Exiting...')
            try:
                sys.exit()
            except SystemExit:
                sys.exit('Decryption failed. Exiting...')
        else:
            continue
# Loop over each word, passing it into the decrypt() method
last_word = word_list[-1]
print(' Attempting decryption...')
success = False
for words in tqdm(word_list):
    brute_force_func()

try:
    sys.exit()
except SystemExit:
    sys.exit('Decryption failed. Exiting...')
