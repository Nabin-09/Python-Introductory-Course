#Blueprint for objects we will use
class Student:
    ...#Placeholder for functions to be placed later

def main():
    student = get_Student()
    print(f"{student.name} from {student.house}")
def get_Student():
    student = Student()
    student.name = input("Name : ")
    student.house = input("House : ")#These are attrebutes/Instance variables
    return student

if __name__ == "__main__":
    main()