import os
from re import S


def require(file, *args):
    with open(os.path.join(os.path.dirname(file), *args), "r") as fh:
        source = fh.read()
    
    return source
