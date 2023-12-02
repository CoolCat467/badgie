from badgie import __main__ as main

assert hasattr(main, "main")
assert callable(main.main)
