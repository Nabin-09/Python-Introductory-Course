try : 
    x = int(input("What is x ? "))
except ValueError:
    print("x is not an integer ")
print(f"x is {x}")#This line isn't indented hence it will run no matter what and return an error

#Will this throw error , Yes it does it throws NameError , x isn't defined
#We can fix this using else