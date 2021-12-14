import os


def require(file, *args):
    with open(os.path.join(os.path.dirname(file), *args), "r") as fh:
        return fh.read()
