#! python3
# selective_copy.py - This program walks through a folder tree and searches for
# files with a certain file extension, provided by the user.
# It then copies these files to a new folder.

import os, shutil

def selective_copy(folder, extension, destination):
    # Walk through the tree
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            # Search for files with a certain extension
            if filename.endswith(extension):
                # Copy these files to a new folder
                file_path = os.path.join(foldername, filename)
                print(str(file_path))
                print('Copying %s...' % (filename))
                shutil.copy(file_path, destination, follow_symlinks=True)
                print('Done.')

folder = input('Enter the path of the folder you wish to search: ')
extension = input('What type of files do you wish to copy (.pdf, .txt, etc.)? ')
destination = input('Enter the path of the destination folder: ')
selective_copy(folder, extension, destination)
