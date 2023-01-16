puzzle = 2.60
doll = 3
bear = 4.10
minion = 8.20
track = 2

tour = float(input())
puzzle_count = int(input())
doll_count = int(input())
bear_count = int(input())
minion_count = int(input())
track_count = int(input())

sum_toys = (puzzle_count + doll_count + bear_count + minion_count + track_count)
price = (puzzle*puzzle_count + doll*doll_count + bear*bear_count + minion*minion_count + track*track_count)
if sum_toys >= 50:
    discount = price*0.25
    price = price - discount

rent = price*0.10
price = price - rent
if tour <= price:
    price = price - tour
    print(f"Yes!{price: .2f} lv left.")
else:
    price = tour - price
    print(f"Not enough money!{price: .2f} lv needed.")
