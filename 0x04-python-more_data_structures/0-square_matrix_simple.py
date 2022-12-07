#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # newList =  [[col**2 for col in row]for row in matrix]
    outer= []
    for row in matrix:
        inner = []
        for col in row:
            [inner.append(col**2)]
        outer.append(inner)
    return outer
