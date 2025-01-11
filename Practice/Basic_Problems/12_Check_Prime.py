def check_prime(n):
    flag = False
    for i in range(2 , n):
        if(n % i == 0):
            return flag
        else :
            continue
    flag = True
    return flag
while True:
    n = int(input("Enter the number ? "))
    if check_prime(n):
        print(f"{n} is prime number")
    else:
        print(f"{n} is not prime number")