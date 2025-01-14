class Student:
    def __init__(self, name , house):#Instance method, it initialise contents of an object from a class
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name : ")
    house = input("House : ")
    student = Student(name , house)