name = input("What is your name ? \n")
file = open("names.txt" , "a")#Open file in write mode , but recreates evertime we run it hence use a and not w
file.write(f"{name}\n")#Writes on text file
file.close()#Closes and saves deprecated use with