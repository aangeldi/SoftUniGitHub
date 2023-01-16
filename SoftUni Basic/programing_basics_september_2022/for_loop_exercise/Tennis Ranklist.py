import math
tournaments = int(input())
points = int(input())
total_points = 0
current_points = 0
win = 0
avarage_points = 0
for i in range (1, tournaments + 1):
    rating = str(input())
    if rating == "W":
        win = win + 1
        current_points = current_points + 2000
    elif rating == "F":
        current_points = current_points + 1200
    elif rating == "SF":
        current_points = current_points + 720

total_points = points + current_points
print(f"Final points: {total_points}")
avarage_points = current_points / tournaments
avarage_points = math.floor(avarage_points)
print(f"Average points: {avarage_points}")
win = (win/tournaments)*100
print(f"{win:.2f}%")