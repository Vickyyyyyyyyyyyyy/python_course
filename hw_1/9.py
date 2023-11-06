# Задание 9

n = int(input('Введите число '))
fact = n

for i in range(1, n):
    fact *= i
print(fact)