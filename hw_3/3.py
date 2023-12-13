#3

import random

class Human:
    def __init__(self, full_name, age, gender):
        self.full_name = full_name
        self.age = age
        self.gender = gender

class Teacher(Human):
    def __init__(self, full_name, age, gender):
        super().__init__(full_name, age, gender)
        self.num_students_taught = 0

    def teach(self, material, *students):
        print(f"{self.full_name} is teaching {material} to students:")
        for student in students:
            student.take(material)
            self.num_students_taught += 1

class Student(Human):
    def __init__(self, full_name, age, gender):
        super().__init__(full_name, age, gender)
        self.knowledge = []

    def take(self, knowledge):
        print(f"{self.full_name} is learning {knowledge}")
        self.knowledge.append(knowledge)

    def forget(self, percentage_to_forget):
        if percentage_to_forget > 0 and percentage_to_forget <= 100:
            forget_count = int(len(self.knowledge) * (percentage_to_forget / 100))
            if forget_count > 0:
                print(f"{self.full_name} is forgetting {forget_count} pieces of knowledge.")
                for _ in range(forget_count):
                    index_to_forget = random.randint(0, len(self.knowledge) - 1)
                    del self.knowledge[index_to_forget]

class EducationalMaterial:
    def __init__(self, *materials):
        self.materials = list(materials)

    def __len__(self):
        return len(self.materials)

class StudentKnowledge:
    def __len__(self):
        return len(self.knowledge)

# Тестирование программы
materials = EducationalMaterial("Python", "Version Control Systems", "Relational Databases", "NoSQL databases", "Message Brokers")

teacher = Teacher("John Doe", 35, "Male")

student1 = Student("Alice Smith", 20, "Female")
student2 = Student("Bob Johnson", 22, "Male")
student3 = Student("Charlie Brown", 21, "Male")
student4 = Student("Diana Davis", 23, "Female")

teacher.teach(materials.materials[0], student1, student2)
teacher.teach(materials.materials[1], student2, student3)
teacher.teach(materials.materials[2], student1, student3, student4)
teacher.teach(materials.materials[3], student4)
teacher.teach(materials.materials[4], student1, student2, student4)

# Вывод знаний каждого ученика
print("\nKnowledge of each student:")
print("Student 1:", student1.knowledge)
print("Student 2:", student2.knowledge)
print("Student 3:", student3.knowledge)
print("Student 4:", student4.knowledge)

# Ученик забывает часть своих знаний
student1.forget(30)
print("\nKnowledge of Student 1 after forgetting:")
print("Student 1:", student1.knowledge)

# Вывод количества обученных учеников у учителя
print("\nNumber of students taught by the teacher:", teacher.num_students_taught)

# Вывод количества материалов и знаний с использованием магических методов
print("\nNumber of materials:", len(materials))
print("Number of knowledge of Student 1:", len(student1.knowledge))
