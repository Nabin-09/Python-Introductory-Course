import csv 
naam = input("What is your name? ")
pata = input("Where do you live? ")
with open("New.csv", "a") as file:
    writer = csv.DictWriter(file , fieldnames=["name","home"])
    writer.writerow({"name":naam , "home":pata})