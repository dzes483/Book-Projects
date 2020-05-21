#!/usr/bin/python3
# gap_inserter.py - This program inserts gaps into numbered files so that a new
# file can be added.

import os
import re

def gap_inserter(folder, filename, file_nr, file_type):
    # Change the directory to run the script
    os.chdir(folder)
    # Loop over the files in the working directory
    file_list = os.listdir(folder)
    print(file_list)
    # Add an empty rename list to add the files to
    rename_list = []
    # Check to see if the filename already exists
    for file in file_list:
        file_number += 1
        if file.startswith(filename + file_nr):
            print(f'File found: {file}') # If so, rename the rest of the files
            print('It exists.')
            file_number += 1
        elif file.startswith(filename):
            # TODO: If not, print message that you are free to move the file
            print('You are free to move this file.')
            rename_list.append(file)
            print(rename_list)
            file_number += 1
            for f in rename_list:
                if file_number == int(file_nr):

gap_inserter('C:\\Users\\Jessica\\AppData\\Local\\Programs\\Python\\Python36\\MyPythonScripts\\My Chapter Projects\\Chapter 9', 'poem', '002', '.txt')
