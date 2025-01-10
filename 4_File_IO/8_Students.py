students = []
with open ("Students.csv") as file:
    for line in file:
        name , house = line.rstrip().split(",")
        student = {} #Creating a dictionary
        student["name"] = name
        student["house"] = house
        """ALternate way
        student = {"name":name , "house":house}
        """
        students.append(student)
def get_name(student):
    return student["name"]
for student in sorted(students , key=get_name):#Sorted function aslo takes key as a parameter
    #We can omit creating the get_name function and create a lambda fucntion instead
    #key = lamda student: student["name"]
    print(f"{student['name']} lives in {student['house']}")
