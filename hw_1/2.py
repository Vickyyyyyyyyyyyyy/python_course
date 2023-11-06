# Задание 2

def maximum_length(str):
    str = ['a', 'b']
    str[0] = input('Напишите строку 1 ')
    str[1] = input('Напишите строку 2 ')
    max_length = max(str, key = len)
    return len(max_length)

print(maximum_length(str))
