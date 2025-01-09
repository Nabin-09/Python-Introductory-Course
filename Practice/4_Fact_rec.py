def factorial(n):
    return 1 if (n==1 or n==0) else n*factorial(n-1)
num = int(input("You want the factorial of ? : "))
print(f"Factorial of {num} is : {factorial(num)} ")