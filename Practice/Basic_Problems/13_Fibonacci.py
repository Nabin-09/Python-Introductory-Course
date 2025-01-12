def Fibonacci(n):
    if n == 1 : return 1 
    if n == 0 : return 0
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
    
n = int(input("Enter the numnber ? "))
print(Fibonacci(n))