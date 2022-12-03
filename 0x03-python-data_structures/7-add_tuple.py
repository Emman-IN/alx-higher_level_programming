#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    tuple_1 = tuple_a + (0, 0)
    tuple_2 = tuple_b + (0, 0)
    new = tuple(map(sum, zip(tuple_1, tuple_2)))
    return new[0], new[1]
