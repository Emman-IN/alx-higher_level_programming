#!/usr/bin/pytho3
def print_reversed_list_integer(my_list=[]):
    new_in_list = my_list[::-1]
    for i in new_in_list:
        print('{:d}'.format(i))
