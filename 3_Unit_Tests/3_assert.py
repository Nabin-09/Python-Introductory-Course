#assert Keyword in Python
#The assert keyword is used for debugging and testing in Python. It checks whether a given condition is True. If the condition evaluates to False, an AssertionError is raised.
from Introduction import square
def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4 
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9 #Throws a long error message, hence use Try except block
    except AssertionError:
        print("3 squared is not 9")
    try:
        assert square(-3) == 9 
    except AssertionError:
        print("-3 squared was not 9")
if __name__ == "__main__":
    main()
#Doing this is pretty dumb actually who is gonna test all the cases
