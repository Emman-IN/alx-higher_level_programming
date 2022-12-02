#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    lens = len(argv) - 1
    if lens == 0:
        print('{} arguements.'.format(lens))
    elif lens == 1:
        print('{} arguement:'.format(lens))
        print('{}: {}'.format(lens, argv[1]))
    else:
        print('{} arguements:'.format(lens))
        for i in range(1, lens+1):
            print('{}: {}'.format(i, argv[i]))
