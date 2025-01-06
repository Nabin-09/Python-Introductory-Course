import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments ")
elif len(sys.argv > 2):
    sys.exit("Too many arguments")
print("My name is ", sys.argv[1])#Had we used the print clause above this line would have ran but as we are using
# the sys.exit clause the program will early exit if the if or elif statement complies  