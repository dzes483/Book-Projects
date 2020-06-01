# !/usr/bin/python3
# picture_grid.py - Prints a flipped copy of the image in the grid.

grid = [['.', '.', '.', '.', '.', '.',], # 0
        ['.', '0', '0', '.', '.', '.',], # 1
        ['0', '0', '0', '0', '.', '.',], # 2
        ['0', '0', '0', '0', '0', '.',], # 3
        ['.', '0', '0', '0', '0', '0',], # 4
        ['0', '0', '0', '0', '0', '.',], # 5
        ['0', '0', '0', '0', '.', '.',], # 6
        ['.', '0', '0', '.', '.', '.',], # 7
        ['.', '.', '.', '.', '.', '.',]] # 8

def printer(grid):
    position = 0
    while position != 6:
        for i in grid:
            print(i[position], end='')
        position += 1
        print('\n')

printer(grid)
