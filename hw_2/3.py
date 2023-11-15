def filter_str_args(*args):
    return tuple(arg for arg in args if isinstance(arg, str))

print(filter_str_args(1,'function', 2, 3, 4, 'Python', 5.0, 'kwargs'))