#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delList = []
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v == value:
                delList.append(k)
        for key in delList:
            del a_dictionary[key]
        return a_dictionary
    return None
