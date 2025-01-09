name = input("What is yout name ? ")
with open ("names.txt", "a") as file:
    file.write(f"{name}\n")