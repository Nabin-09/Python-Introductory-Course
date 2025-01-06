#We can make our custom Libraries as well
def hello(name):
    print(f"Hello my name is {name}")
def goodbye(name):
    print(f"Goodbye, {name}")

def main():
    hello("Nabin")
    goodbye("Nabin")
#If we have a main function in libraries , then no matter what function we call in the later file
# but the main function will run. hence , avoid writing main functions in parent library
if __name__ == "__main__":
    main()