"""with open("names.txt" , "r") as file:#we can omit r as well as it is the default
    lines = file.readlines()

for line in lines:
    print("hello ,",line, end="")#or use print("hello,",line.rstrip()) for removing lines """
#Sorting and printing them 
"""names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello , {name}")"""
# More efficient way to do this
with open("names.txt") as file:
    for line in sorted(file):
        print("hello",line.rstrip())