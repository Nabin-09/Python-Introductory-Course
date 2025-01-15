n = int(input("Enter the last number of series : "))
sum = 0 
for i in range(1,n+1):
    sum += i*i
print(f"Sum of squares till {n} is :",sum)
"""
def squaresum(n):
    return(n*(n+1)*(2*n+1))//6
    This will work too
"""