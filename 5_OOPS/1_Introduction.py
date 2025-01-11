def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")

def get_name():
    name = input("Enter your name : ")
    return name
def get_house():
    name = input("Enter your house : ")
    return name
if __name__ == "__main__":
    main()