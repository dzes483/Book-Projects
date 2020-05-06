#! python3
# brute_force.py - Attempts to decrypt an encrypted PDF file by trying every
# possible English word until it finds one that works.

import PyPDF2
from tqdm import tqdm
import sys

# Open the dictionary file
word_doc = open('dictionary.txt', 'r')

# Read the dictionary file line-by-line
words = word_doc.readlines()

# Open the encrypted PDF
pdf_doc = input('Enter the name of the PDF file you want to decrypt: ')
pdf_reader = PyPDF2.PdfFileReader(open(pdf_doc, 'rb'))

# Create a list of word strings by reading the file and strip off the
# whitespace characters
word_list = []
for word in words:
    word_list.append(word.strip().split())


def brute_force_func():
    # Loop over each word, passing both the upper and lowercase forms into the
    # decrypt() method
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

# Loop over each word
last_word = word_list[-1]
print(' Attempting decryption...')
success = False
for words in tqdm(word_list):
    brute_force_func()

try:
    sys.exit()
except SystemExit:
    sys.exit('Exiting...')
