#! python3
# blank_row_inserter.py - Takes two integers and a filename string as arguments.
# Starting at row num (first integer), the program inserts num_rows (second integer)
# blank rows into the spreadsheet.

import openpyxl

# Get the user's input
while True:
    while True:
        file_name = input('Enter the filename (the final document will be saved as a copy): ')
        if file_name.endswith('.xlsx'):
            break
        else:
            print('File is not in .xlsx format.')
            continue
    while True:
        try:
            num = int(input('Enter the row number to begin at: '))
            num_rows = int(input('Enter the number of rows to insert: '))
        except ValueError:
            print("You've entered an invalid character. Please enter a number. ")
            continue
        else:
            break

    # Read the contents of the spreadsheet
    try:
        wb_source = openpyxl.load_workbook(file_name)
    except FileNotFoundError:
        print("We couldn't find that file. Check the spelling and that it exists in the current directory")
        continue
    else:
        break

source_sheet = wb_source.active

source_sheet.insert_rows(num, amount=num_rows)

wb_source.save('Copy of '+ file_name)
print('New file saved.')
