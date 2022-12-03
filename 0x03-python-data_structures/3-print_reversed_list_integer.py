#!/usr/bin/pytho3
"""Prints a list in a reersed order"""
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list), 0, -1):
        print(i)
