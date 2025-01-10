# we have a csv module in Python for us
import csv
students = []

with open("Students.csv") as file:
    reader = csv.reader(file) # reader function reads a csv for us
    for name,home in reader:
        students.append({"name":name,"home":home})

for student in sorted(students, key= lambda student:student["name"]):
    print(f"{student['name']} is from {student['home']}")