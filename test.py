password = "ppp_"

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