# array = [222, 32, 45, 1, 26, 22, -32, -212, -22]
# array_str = str(array)
# array_str = array_str[1:][:-1]
# print(array_str)
# a = array_str.split(", ")
#
# print(a)
#
# # txt = "234"
# for i in range(len(a)):
#     print(a[i])

a = "asdfg"
b = ""
c = []
for i in range(len(a) - 1, -1, -1):
    b = b + a[i]
    c.append(a[i])
print(b)
print(c)

