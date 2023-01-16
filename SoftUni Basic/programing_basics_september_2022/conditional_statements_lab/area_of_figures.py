import math
from math import pi

figure = str(input())

if figure == "square":
    a = float(input())
    result = a*a
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    result = a * b
elif figure == "circle":
    r = float(input())
    r **= 2
    result = pi * r
elif figure == "triangle":
    a = float(input())
    h = float(input())
    result = (a * h)/2
print(f"{result: .3f}")
