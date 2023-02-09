import math

N = int(input())
P = int(input())
courses = N / P
courses = math.ceil(courses)

print(courses)