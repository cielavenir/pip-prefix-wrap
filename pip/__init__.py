import sys
if True:
    # load original pip
    # using technique described in https://qiita.com/cielavenir/items/8d3ca1b6a0b6298b4d55
    from os.path import dirname
    from os.path import realpath
    from importlib import reload
    sys_path_orig = sys.path[:]
    myroot = realpath(dirname(dirname(__file__)))
    for i in range(len(sys.path)-1,-1,-1):
        if realpath(sys.path[i]) == myroot:
            sys.path.pop(i)
    import pip
    reload(pip)
    sys.path[:] = sys_path_orig

import os
if os.name == 'posix':
    # implement https://github.com/pypa/pip/pull/13634 by monkey-patch
    import pip._internal.locations._sysconfig as locations_sysconfig
    def _infer_prefix():
        return 'posix_prefix'
    locations_sysconfig._infer_prefix = _infer_prefix
    del _infer_prefix
    del locations_sysconfig
    import pip._internal.build_env as build_env
    def get_runnable_pip():
        return os.path.join(os.path.dirname(__file__), '__pip-runner__.py')
    build_env.get_runnable_pip = get_runnable_pip
    del get_runnable_pip
    del build_env
