sea_trip = int(input())
mountain_trip = int(input())
counter =  0
sum = 0

while sea_trip != 0 or  mountain_trip != 0:
    trip_type = str(input())
    if trip_type == "sea" and sea_trip != 0:
       sum = sum + 680
       sea_trip = sea_trip - 1
    elif trip_type == "mountain" and mountain_trip != 0:
       sum = sum + 499
       mountain_trip = mountain_trip - 1
    elif trip_type == "Stop":
        sum = sum + 0
        counter = counter + 1
        break

if counter == 0:
    print(f"Good job! Everything is sold.")
    print(f"Profit: {sum} leva.")
else:
    print(f"Profit: {sum} leva.")