
# x = int(input("What is x ? "))
# print(f"x is {x}") #Throws ValueError if I enter a string like "Nabin"

try: 
    x = int(input("What is x ? "))
    print(f"x is {x}")
except ValueError: 
    print("x is not an integer ")
