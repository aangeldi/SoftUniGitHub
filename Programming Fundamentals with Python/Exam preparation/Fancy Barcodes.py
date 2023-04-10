import re
n = int(input())

for i in range(n):
    barcode = input()

    pattern_barcode = r"@#+[A-z][A-Za-z\d]+[A-Z]@#+"
    pattern_digits = r"\d+"