#!/usr/bin/python3
# big_file_hunter.py - Searches the specified path for the biggest files
# (>1000mb) and displays these files with their absolute paths to the screen.

import os

# Walk through the tree
def file_hunter(folder):
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            size = os.path.getsize(file_path)
            # Define a size in mb for user readability
            size_mb = size * .000001
            # Find files over 1000mb
            if size > 100000000:
                # Print the file paths and sizes to the screen
                print('File path: %s' % (file_path))
                print(f'File size: {size} bytes (%.2f megabytes)' % size_mb)
                print('\n')
                break
        break
    else:
        print('No large files found.')

folder = input('Enter the path of the folder that you wish to search: ')

file_hunter(folder)
