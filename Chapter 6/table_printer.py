#! python3
# table_printer.py - Takes a list of lists of strings and displays it in a
# well-organized table with each column right-justified.

table_data = [['apples', 'oranges', 'cherries', 'bananas'],
                ['Alice', 'Bob', 'Carol', 'David'],
                ['dogs', 'cats', 'moose', 'geese']]

def printTable(data):
    for j in range(len(data[0])):
        for i in range(len(data)):
            #This line finds the longest item for each list and its length
            x = len(max(data[i], key=len))
            print(data[i][j].rjust(x), end=' ')
        print()

printTable(table_data)
