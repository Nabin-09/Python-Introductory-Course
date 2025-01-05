#raise keyord
# The raise keyword in Python is used to trigger an exception. You can use it to manually raise an exception when a certain condition is met or when an error needs to be explicitly brought to attention.
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    print(check_age(14))
except ValueError as e:
    print(e)
