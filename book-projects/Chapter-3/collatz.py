# !/usr/bin/python3
# collatz.py - Takes in an integer repeatedly until the output reaches 1,
# demonstrating the Collatz sequence.

def collatz(num):
    if num % 2 == 0:
        num = num/2
        print(int(num))
        return num
    else:
        num = (3*num) + 1
        print(int(num))
        return num

while True:
    try:
        num = int(input('Enter a number: '))
        break
    except ValueError:
        print('That is not a number. Please enter an integer.')
        continue

while num != 1:
    num = collatz(num)
