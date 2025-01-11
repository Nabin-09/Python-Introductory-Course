#Dictionaries are key value pairs
def main():
    Student  = get_student()
    print(f"{Student['name']} from {Student['house']}")#Indexing a tuple

def get_student():
    Student = {}
    Student["name"] = input("Name : ")
    Student["house"] = input("House : ")
    return Student 

if __name__ == "__main__":
    main()