
def check_type(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, int):
            raise TypeError("Неверный тип данных")
        return result
    return wrapper

@check_type
def func1(a, b):
    return a + b

@check_type
def func2(a, b):
    return a * b


print(func1(1,3))
print(func2(5.1,1))