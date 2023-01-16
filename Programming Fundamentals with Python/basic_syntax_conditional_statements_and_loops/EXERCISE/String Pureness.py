n = int(input())

for i in range(n):
    string = str(input())
    for j in range(len(string)):
        if string[j] != "," and string[j] != "." and string[j] != "_":
            continue
        else:
            print(f"{string} is not pure!")
            break
    else:
        print(f"{string} is pure.")



