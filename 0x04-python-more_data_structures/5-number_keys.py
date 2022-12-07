#!/usr/bin/python3
def common_elements(set_1, set_2):
    new = set()
    for item in zip(set_1, set_2):
        if set_1 == set_2:
            new.add(set_1)
    return new
