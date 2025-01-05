def main ():
    x = get_init()
    print(f"x is {x}")
def get_init():
    while True:
        try:
            x = int(input("What is x ?"))
            return x
        except ValueError:
            print("x is not an integer")
        else: #we can omit this else statement 
            return x

main()    