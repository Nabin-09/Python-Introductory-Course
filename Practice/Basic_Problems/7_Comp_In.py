p , r, t =  map(float , input("Enter the values of Principle , rate and time in years : ").split())
Amount = p * (pow((1 + r / 100), t))
print("Total compound interest : ",Amount - p)