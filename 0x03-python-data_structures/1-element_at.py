#!/usr/bin/python3
"""Replace element a an index"""
def element_at(my_list, idx):
    if 0 <= idx <= len(my_list)-1:
        return my_list[idx]
    return None
