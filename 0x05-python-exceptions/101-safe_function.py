#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
        return res
    except Exception as ex:
        sys.stderr.write("Exception: {}\n".format(ex))
        return None
