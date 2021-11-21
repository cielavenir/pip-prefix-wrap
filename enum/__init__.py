import sys
if sys.version_info>=(3,4):
    # if somehow loaded on Python 3.4+ (possibly by buggy PYTHONPATH), should load original enum
    # using technique described in https://qiita.com/cielavenir/items/8d3ca1b6a0b6298b4d55
    from os.path import dirname
    from os.path import realpath
    from importlib import reload
    myroot = realpath(dirname(dirname(__file__)))
    for i in range(len(sys.path)-1,-1,-1):
        if realpath(sys.path[i]) == myroot:
            sys.path.pop(i)
    import enum
    reload(enum)
    __all__ = enum.__all__
    from enum import *
else:
    import aenum
    __all__ = aenum.__all__
    from aenum import *
