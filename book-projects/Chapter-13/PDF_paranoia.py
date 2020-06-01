#!/usr/bin/python3
# PDF_paranoia.py - Encrypts every PDF in a folder and its subfolders using a
# provided password. It adds the suffix "_encrypted.pdf" to each newly-
# encrypted file.

import os
import PyPDF2
from pathlib2 import Path


path = input('Input the full path of the folder you wish to search: ')
secret_key = input('Enter the desired encryption password: ')

# Loop through the directory and their subdirectories, searching for PDF files.
for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        file_path = os.path.join(root, name)
        if file_path.endswith('.pdf'):
            pdf_file = open(file_path, 'rb')
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            # Skip the file if it is already encrypted.
            if pdf_reader.isEncrypted:
                pass
            else:
                # Otherwise, encrypt the document using the user's choice of a
                # password.
                print('Encrypting ' + name + '...')
                pdf_writer = PyPDF2.PdfFileWriter()
                for page_num in range(pdf_reader.numPages):
                    # Rewrite the file, page by page.
                    pdf_writer.addPage(pdf_reader.getPage(page_num))
                    pdf_writer.encrypt(secret_key)
                    # Rename the new, encrypted file.
                    new_name = os.path.splitext(name)[0]+'_encrypted.pdf'
                    result_pdf = open(new_name, 'wb')
                    pdf_writer.write(result_pdf)
                    result_pdf.close()

print('Done.')
