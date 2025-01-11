def Sieve_Of_Eratosthene(n):
    primes = [True]*(n+1)
    primes[0], primes[1] = False , False

    for i in range(2 , int(n ** 0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1 , i):
                primes[j] = False
    return [i for i in range(n+1) if primes[i]]

n= 50
print(f"Prime numbers upto {n} : ",Sieve_Of_Eratosthene(n))