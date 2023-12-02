from badgie import _version

assert isinstance(_version.__version__, str)
assert "." in _version.__version__
