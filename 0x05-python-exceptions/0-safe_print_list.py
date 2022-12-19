#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    len = 0
    for i in my_list:
        len += 1
    for j in range(0, x):
        try:
            print('{}'.format(my_list[j]), end="")
        except IndexError:
            x = len
    print()
    return x
