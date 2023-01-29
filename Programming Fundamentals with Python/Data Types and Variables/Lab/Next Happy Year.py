# You are saying goodbye to your best friend: "See you next happy year".
# Happy Year is the year with only distinct digits, for example, 2018.
# Write a program that receives an integer number and finds the next happy year.

year = int(input())
year += 1
year_str = str(year)
temp = set(year_str)

while len(year_str) != len(temp):
    year += 1
    year_str = str(year)
    temp = set(year_str)
print(year)
