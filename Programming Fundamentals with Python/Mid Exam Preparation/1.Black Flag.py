days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
total_plunder = 0
percentage = 0

for day in range(1, days + 1):
    total_plunder += daily_plunder
    if day % 3 == 0:
        total_plunder += 0.5 * daily_plunder
    if day % 5 == 0:
        total_plunder -= 0.3 * total_plunder
    
if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    percentage = (100 / expected_plunder) * total_plunder
    print(f"Collected only {percentage:.2f}% of the plunder.")