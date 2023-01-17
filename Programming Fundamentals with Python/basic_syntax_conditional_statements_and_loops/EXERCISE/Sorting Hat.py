name = ""

while name != "Welcome!":
    name = str(input())
    length = len(name)
    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    if name == "Welcome!":
        print("Welcome to Hogwarts.")
    elif length < 5:
        print(f"{name} goes to Gryffindor.")
    elif length == 5:
        print(f"{name} goes to Slytherin.")
    elif length == 6:
        print(f"{name} goes to Ravenclaw.")
    elif length > 6:
        print(f"{name} goes to Hufflepuff.")
