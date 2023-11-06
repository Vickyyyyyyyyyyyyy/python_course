# Задание 10

lst = [2, 4, 5, 8, 9, 13]

for number in range(len(lst)):
    lst[number] *= number
print(lst)


number = 0
if number >= 0 and number < len(lst):
    lst[number] *= number
print(lst)