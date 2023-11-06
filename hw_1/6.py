# Задание 6
from random import randint

mylist = []
count = 0

for i in range(5):
    mylist.append(randint(-100, 100))
print (mylist)

for i in mylist:
    if i>0:
        count+= 1
print(count)








