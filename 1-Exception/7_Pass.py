#If we use the pass keyword nothing happens further and no prompt is shows it simply continues
def main ():
    x = get_init()
    print(f"x is {x}")
def get_init():
    while True:
        try:
            x = int(input("What is x ?"))
            return x
        except ValueError:
            pass

main()    