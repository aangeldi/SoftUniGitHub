def palindrome(txt):
    invert = []
    for word in txt:
        temp = ""
        for j in range(len(word) - 1, -1, -1):
            temp = temp + word[j]
        invert.append(temp)

    for i in range(len(txt)):
        if txt[i] == invert[i]:
            print("True")
        else:
            print("False")


lists = input().split(", ")
palindrome(lists)
