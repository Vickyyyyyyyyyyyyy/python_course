#1

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def task1(self):
        return self.a * self.b
    def task2(self):
        return 2*(self.a + self.b)

r1 = Rectangle(2,3)

print(r1.task1())
print(r1.task2())



