#!/usr/bin/python3
# table_printer.py - Takes a list of lists of strings and displays it in a
# well-organized table with each column right-justified.

table_data = [['apples', 'oranges', 'cherries', 'bananas'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'geese']]


def printTable(data):
    for i in range(len(data[0])):   # for each list in the data
        for j in range(len(data)):  # for each item in the lists
            # Find the longest item and its length.
            x = len(max(data[j], key=len))
            print(data[j][i].rjust(x), end=' ')
        print()

printTable(table_data)
