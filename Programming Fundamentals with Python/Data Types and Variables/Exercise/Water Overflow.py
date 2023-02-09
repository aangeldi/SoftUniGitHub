water_tank = 255
n = int(input())
result = 0
for i in range(n):
    liters_of_water = int(input())
    result += liters_of_water
    if result > water_tank:
        print("Insufficient capacity!")
        result -= liters_of_water
        continue
print(result)

