#!/usr/bin/python3
if __name__ == "__main__":
    form sys import argv
    lens = len(sys.argv) - 1
    sep = [':', '.']
    if lens == 0:
        print('{} arguements{}'.format(lens, sep[1]))
    else:
        if lens == 1:
            print('{} arguement{}'.format(lens, sep[0]))
            print('{}{} {}'.format(1, sep[0], argv[1]))
        else:
            print('{} arguements{}'.format(lens, sep[0]))
            for i in range(1, lens+1):
                print('{}{} {}'.format(i, sep[0], argv[i]))
