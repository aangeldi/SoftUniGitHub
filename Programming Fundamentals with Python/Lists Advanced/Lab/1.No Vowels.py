text = input()
no_vowels = [char for char in text if char.lower() not in ['a', 'o', 'u', 'e', 'i']]

print(*no_vowels, sep="")