student = []
with open("Students.csv") as file:
    for line in file:
        name,house = line.rstrip().split(",")
        student.append(f"{name} lives in {house}")

for student in sorted(student):
    print(student)#This actually sorts wrt the whole sentence and not only name
