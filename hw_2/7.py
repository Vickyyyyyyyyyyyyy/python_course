def retry_on_exception(max_retries=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print("Перезапуск")
                    retries += 1
            raise RuntimeError("максимальное кол-во перезапусков. задача не решена")

        return wrapper

    return decorator


from random import randint

@retry_on_exception()
def divide(a, b):
    return a / b

@retry_on_exception(max_retries=5)
def generate_random():
    if randint(0, 1) == 0:
        raise ValueError("Random error")
    return "Выполнено"

print(divide(1,2))
print (generate_random())

