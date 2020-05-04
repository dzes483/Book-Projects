#! python3
# text_files_to_spreadsheet.py - Reads in the contents of several text files
# and inserts the contents into a spreadsheet, with one line of text per row.
# The lines of the first text file will be found in the cells of column A, the
# lines of the second in the cells of column B, and so on.

import openpyxl
import os

# Get the file names
file_list = []


def file_input():
    while True:
        file = input('Enter the .txt file you wish to move to Excel: ')
        # Check that the file is a .txt file
        if file.endswith('.txt'):
            # Check that the file exists
            exists = os.path.isfile(file)
            # If it does, then append the file name to the file list
            if exists:
                file_list.append(file)
                break
            else:
                print('File does not exist. Please enter a valid file name or'
                      ' path.')
                continue
        else:
            print('Invalid file format. Please only enter a .txt file.')
            continue

new_file_name = str(input('Enter the desired name for your new file: '))
while True:
    file_input()
    another = input('Would you like to enter an additional file? Yes or no? ')
    if another.upper() == 'N':
        print('Okay, continuing...')
        break
    elif another.upper() == 'Y':
        continue
    else:
        print("Please enter either 'Yes' or 'No'.")
        continue

# Read the content of the files
content_list = []
for f in file_list:
    with open(f, 'r') as f:
        content = f.readlines()
        content_list.append(content)

# Open a blank workbook and define the sheet
print('Creating workbook...')
wb = openpyxl.Workbook()
sheet = wb.active
row_counter = 1
col_counter = 1
# Loop through the filenames in the content list
for i in content_list:
    # Loop through the lines in the files
    for line in i:
        # Add the line's value to the cell
        sheet.cell(row=row_counter, column=col_counter).value = line
        row_counter += 1
    # Reset the row counter to 1 for the next file
    row_counter = 1
    col_counter += 1

wb.save(new_file_name + str('.xlsx'))

print('Done.')
