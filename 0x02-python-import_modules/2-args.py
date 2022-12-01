#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_len = len(sys.argv) - 1
    sep = [':', '.']
    if arg_len == 0:
        print('{} arguement{}'.format(arg_len, sep[1]))
    else:
        print('{} arguements{}'.format(arg_len, sep[0]))
        for i in range(1, arg_len+1):
            print('{}{} {}'.format(i, sep[0], sys.argv[i]))
