## pip-prefix-wrap

Wraps pip to force posix_prefix scheme on posix platform. This is convenient to create environments using `--prefix=` for Debian systems.

install:

You need to bootstrap with patched setuptools or you cannot install this pip to expected path :sweat:

```
# export PYTHONPATH=/foo/bar
git clone https://github.com/cielavenir/setuptools.git
cd setuptools
git checkout origin/v78.1.1-patchscheme
python3 setup.py install --prefix=/foo/bar
cd ..

git clone https://github.com/cielavenir/pip-prefix-wrap.git
cd pip-prefix-wrap
python3 setup.py install --prefix=/foo/bar
cd ..
```

note: when you add this pip monkeypatch to PYTHONPATH, you must specify --prefix (or --home), or you will clobber system unexpectedly (i.e. do not pass PYTHONPATH when running sudo).

## Pull Requests

- https://github.com/pypa/distutils/pull/378
- https://github.com/pypa/pip/pull/13634
