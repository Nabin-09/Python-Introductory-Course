#Blueprint for objects we will use
class Student:
    ...

def main():
    student = get_Student()
    print(f"{student.name} from {student.house}")
def get_Student():
    student = Student()
    student.name = input("Name : ")
    student.house = input("House : ")
    return student

if __name__ == "__main__":
    main()