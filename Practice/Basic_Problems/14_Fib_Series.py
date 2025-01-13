def Fibonacci(n):
    a, b = 0, 1  # First two Fibonacci numbers
    for _ in range(n):  
        print(a, end=" ")  # Print current Fibonacci number
        a, b = b, a + b  # Update for the next step

n = int(input("n : "))
Fibonacci(n)
