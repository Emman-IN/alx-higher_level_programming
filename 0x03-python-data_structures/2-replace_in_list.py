#!/usr/bin/python3
"""function that replaces an element of a list at a specific position"""
ef replace_in_list(my_list, idx, element):
    if 0 <= idx <= len(my_list)-1:
        my_list[idx] = element
        return my_list
    return my_list
