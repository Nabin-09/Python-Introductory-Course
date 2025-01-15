def CubeSum(n):
    sum = 0
    for i in range(1, n+1):
        sum+=i*i*i
    return sum
n = int(input("Enter the last number of series : "))
print(f"Sum of cubes of numbers till {n} :",CubeSum(n))