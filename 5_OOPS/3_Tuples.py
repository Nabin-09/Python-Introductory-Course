#Tuples are collection of values but immutable
def main():
    Student  =get_student()
    print(f"{Student[0]} from {Student[1]}")#Indexing a tuple

def get_student():
    name = input("Name : ")
    house = input("House : ")
    return (name,house)#Tuples are used defensively to stop changes

if __name__ == "__main__":
    main()