#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        res = fct(*args)
        return res
    except Exception as ex:
        sys.stderr.write("Exception: {}\n".format(ex))
        return None
