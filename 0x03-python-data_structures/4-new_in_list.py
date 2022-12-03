#!/usr/bin/python3
"""replaces an element in a list at a specific position without modifying the original list """
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if 0 <= idx <= len(my_list)-1:
        new_list[idx] = element
        return new_list
    return my_list
