

# class Student:
#     pass

class Student:
    def __init__(self,name=None, age=None, grade=None):
        self.name=name
        self.age=age
        self.grade=grade

    def __str__(self):
        return f"Student(name={self.name}, age={self.age}, grade={self.grade})"    
    

    def getFullName1(self):
        return f'{self.name} {self.age}'
    
    @staticmethod
    def getFullName(student):
        return f'{student.name} {student.age}'


student1=Student("Alice1", 20, "A")
student2=Student("Bob1", 22, "B")

# student1.name = "Alice"
# student1.age = 20
# student2.name = "Bob"
# student2.age = 22

# student1.grade = "A"
# student2.grade = "B"

print(f"{student1.name}")
print(f"{student2.name}")
print(student1)
print(student2)
print(student1.__str__())
print(student2.__str__())

# print(student1.getFullName())
# print(student2.getFullName())

print(Student.getFullName(student1))