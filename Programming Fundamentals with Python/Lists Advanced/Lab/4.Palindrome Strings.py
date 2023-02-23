strings = input().split()
searched_palindrome = input()
palindrome = []
counter_palindrome = 0
for word in strings:
    if word == "".join(reversed(word)):
        palindrome.append(word)
    if word == searched_palindrome:
        counter_palindrome += 1

print(palindrome)
print(f"Found palindrome {counter_palindrome} times")
