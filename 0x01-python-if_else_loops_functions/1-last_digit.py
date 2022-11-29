#!/usr/bin/python3
import random
number = -98
last = abs(number) % 10
if number >= 0:
    if last > 5:
        print(f'Last digit of {number:d} is {last:d} and is greater than 5')
    elif last == 0:
        print(f'Last digit of {number:d} is {last:d} and is 0')
else:
    if number < 0:
            print(f'Last digit of {number:d} is {last*-1:d} and is less than 6 and not 0')
