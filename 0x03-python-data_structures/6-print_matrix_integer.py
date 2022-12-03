#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """convert each sublist to a string seperated by space """
    for item in matrix:
        print('{}'.format(' '.join(map(str, item))))
