import datetime

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        duration = end_time - start_time
        print(f"Время выполнения функции: {duration.total_seconds()} секунд")
        return result

    return wrapper


@timer
def filter_str_args(*args):
    return tuple(arg for arg in args if isinstance(arg, str))

print(filter_str_args(1,'function', 2, 3, 4, 'Python', 5.0, 'kwargs'))

