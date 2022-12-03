#!/usr/bin/python3
def max_integer(my_list=[]):
    """Bubble sort"""
    if my_list:
        for i in range(len(my_list)):
            for j in range(1, len(my_list)):
                if my_list[j] > my_list[i]:
                    max = my_list[i]
                    my_list[i] = my_list[j]
                    my_list[j] = max
        return my_list[0]
    return None
