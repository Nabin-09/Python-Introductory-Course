import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("My name is ",arg)
"""
 python 6_Nametags.py Nabin Sharma nitin sudha
 My name is  6_Nametags.py
My name is  Nabin
My name is  Sharma
My name is  nitin
My name is  sudha
we should slice to remove the name of program
"""