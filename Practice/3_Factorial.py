num = int(input("You want factorial of ? : "))
factorial = 1
for i in range(1, num +1):
    factorial *= i
print(f"Factorial of {num} is : {factorial}")