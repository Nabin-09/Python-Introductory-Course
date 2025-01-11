def Area_Circle(r):
    pi = 3.142
    area = pi * r * r
    return area
r = int(input("What is the radius of r ? "))
print(f"Area of circle is : {Area_Circle(r)}")