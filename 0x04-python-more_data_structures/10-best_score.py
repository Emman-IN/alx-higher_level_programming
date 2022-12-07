#!/usr/bin/python3
def best_score(a_dictionary):
    valueSorted = dict(sorted(a_dictionary.items(),
                       key=lambda x: x[1]), reverse=True)
    first = list(valueSorted.keys())[0]
    return str(first)
