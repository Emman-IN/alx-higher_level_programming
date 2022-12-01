#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lens = len(sys.argv) - 1
    l = [':', '.']
    if lens == 0:
        print('{} arguement{}'.format(lens, l[1]))
    else:
        print('{} arguements{}'.format(lens, l[0]))
        for i in range(1, lens+1):
            print('{}{} {}'.format(i, l[0], sys.argv[i]))

