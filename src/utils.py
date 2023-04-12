import errno
import os


def make_dirs(path):
    try:
        os.makedirs(path)
    except OSError as e:
        if errno.EEXIST != e.errno:
            raise
