# High = 89#Low = 28#Medium = 77#Low = 23
fires_cells = input().split("#")
water = int(input())
total_fire = 0
effort = 0
value_used = []
for cell in fires_cells:
    temp = cell.split(" = ")
    level = temp[0]
    value = int(temp[1])
    if level == "High" and (81 > value or value > 125):
        continue
    elif level == "Medium" and (51 > value or value > 80):
        continue
    elif level == "Low" and (1 > value or value > 50):
        continue

    if water >= value:
        total_fire += value
        water -= value
        value_used.append(value)

effort = total_fire * 0.25
print(f"Cells:")
for i in value_used:
    print(f" - {i}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
