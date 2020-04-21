#! python3
# gap_filler.py - Finds all files with a given prefix (such as file001, file002,
#, etc.) in a single folder and locates any gaps in the numbering (for example,
# if there is a file001 and file003, but no file002). The program will rename
# all of the files to close this gap.

import os, re

def gap_filler(folder, prefix, suffix):
    # Change the directory to run the script
    os.chdir(folder)
    # Loop over the files in the working direct
    file_list = os.listdir(folder)
    # Create an empty list for renaming the files
    rename_list = []
    # Find files that begin with the desired prefix
    for i in file_list:
         if i.startswith(prefix):
             print(f'File found: {i}')
             # Add the matching files to the rename_list
             rename_list.append(i)
    # See if the files end with the correct number
    file_number = 1
    for i in rename_list:
         # If so, then move on to the next number
         if i.endswith(f'{file_number}{suffix}'):
             print(f"{i}'s number is correct.")
             file_number += 1
         # If not, then rename the file and move on to the next number
         else:
            print(f'Renaming {i}...')
            if file_number in range(1,10):
                new_name = prefix + '00' + str(file_number) + suffix
            elif file_number in range(10,100):
                new_name = prefix + '0' + str(file_number) + suffix
            elif file_number in range(100,1000):
                new_name = prefix + '0' + str(file_number) + suffix
            os.rename(i, i.replace(i, new_name))
            file_number +=1

folder = input('Enter the folder you want to search: ')
prefix = input('Enter the file prefix (not including the numbers): ')
suffix = input('Enter the file type (.txt, .jpg, .pdf, etc.): ')

gap_filler(folder, prefix, suffix)
