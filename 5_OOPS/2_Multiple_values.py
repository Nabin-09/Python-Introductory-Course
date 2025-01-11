def main():
    name , house =  get_student()
    print(f"{name} from {house}")
def get_student():
    name = input("Name : ")
    house = input("House : ")
    return name , house #If we return like this the order is maintained while receiving

if __name__ == "__main__":
    main()