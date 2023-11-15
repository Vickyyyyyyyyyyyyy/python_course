numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = 2

print(list(filter(lambda x: x%a == 0, numbers)))