command = ""

while command != "End":
    command = str(input())
    new_str = ""
    if command == "SoftUni" or command == "End":
        continue
    else:
        for i in range(len(command)):
            a = command[i] + command[i]
            new_str += a
        print(f"{new_str}")
