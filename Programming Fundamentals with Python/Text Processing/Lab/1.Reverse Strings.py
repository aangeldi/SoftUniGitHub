word = input()

while word != "end":
    invert_word = ""
    for i in reversed(word):
        invert_word += i
    print(word + " = " + invert_word)
    word = input()