password = input()

while True:
    line = input()
    if line == "Complete":
        break

    command = line.split(" ")

    if command[0] == "Validation":
        if len(password) < 8:
            print("Password must be at least 8 characters long!")
        if not all(ch.isalnum() or ch == "_" for ch in password):
            print("Password must consist only of letters, digits and underscore!")
        if not any(ch.isupper() for ch in password):
            print("Password must consist at least one uppercase letter!")
        if not any(ch.islower() for ch in password):
            print("Password must consist at least one lowercase letter!")
        if not any(ch.isdigit() for ch in password):
            print("Password must consist at least one digit!")

    elif command[0] == "Make":
        index = int(command[2])
        if index < 0 or index >= len(password):
            continue
        if command[1] == "Upper":
            password = password[:index] + password[index].upper() + password[index + 1:]
        elif command[1] == "Lower":
            password = password[:index] + password[index].lower() + password[index + 1:]
        print(password)

    elif command[0] == "Insert":
        index = int(command[1])

        if len(password) > index >= -len(password):
            password = password[:index] + command[2] + password[index:]
            print(password)

    elif command[0] == "Replace":
        char = command[1]
        if char not in password:
            continue
        value = int(command[2])
        new_char = chr(ord(char) + value)
        password = password.replace(char, new_char)
        print(password)

    else:
        continue
