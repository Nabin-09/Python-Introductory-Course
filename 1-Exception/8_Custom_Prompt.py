def main():
    x = get_int("What is value of x? ")
    print(f"x is {x} ")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()