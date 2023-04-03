data = input().split(", ")
others = "-_"

for el in data:
    if 16 >= len(el) >= 3:
        temp = ""
        for i in range(len(el)):
            if el[i] in others or el[i].isalpha() or el[i].isdigit():
                temp += el[i]

        if len(temp) == len(el):
            print(el)
