#2

class Teacher:
    def __init__(self):
        self.num_students_taught = 0

    def teach(self, material, *students):
        print(f"Teacher is teaching {material} to students:")
        for student in students:
            student.take(material)
            self.num_students_taught += 1

class Student:
    def __init__(self):
        self.knowledge = []

    def take(self, knowledge):
        print(f"Student is learning {knowledge}")
        self.knowledge.append(knowledge)

class EducationalMaterial:
    def __init__(self, *materials):
        self.materials = list(materials)

# Тестирование программы
materials = EducationalMaterial("Python", "Version Control Systems", "Relational Databases", "NoSQL databases", "Message Brokers")

teacher = Teacher()

student1 = Student()
student2 = Student()
student3 = Student()
student4 = Student()

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

# Вывод количества обученных учеников у учителя
print("\nNumber of students taught by the teacher:", teacher.num_students_taught)
