command = ""
count = 0

while command != "END":
    command = str(input())

    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        count += 1
    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        count += 2
    else:
        continue

if count > 5:
    print(f"You need extra sleep")
else:
    print(f"{count}")