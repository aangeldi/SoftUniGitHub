def password_func(password):
    counter = 0
    not_letter = 0
    for i in range(len(password)):
        if 48 <= ord(password[i]) <= 57:
            counter += 1
        elif 9 < ord(password[i]) < 65 or 90 < ord(password[i]) < 97 or ord(password[i]) > 122:
            not_letter += 1

    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")
    if not_letter != 0:
        print("Password must consist only of letters and digits")
    if counter < 2:
        print("Password must have at least 2 digits")
    if 6 <= len(password) <= 10 and not_letter == 0 and counter >= 2:
        print("Password is valid")


pass_word = input()
password_func(pass_word)
