array = [23, 12, -334, 1000, 3, -2, 111]
temp = 0

#sorting of the array
for i in range(len(array)):
    for j in range(len(array) - 1):
        if array[j] < array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]  #swap
            # appropriation

            # temp = array[j]
            # array[j] = array[j + 1]
            # array[j + 1] = temp

print(array)

