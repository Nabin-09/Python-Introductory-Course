#Tuples are collection of values but immutable
def main():
    Student  =get_student()
    print(f"{Student[0]} from {Student[1]}")

def get_student():
    name = input("Name : ")
    house = input("House : ")
    return (name,house)

if __name__ == "__main__":
    main()