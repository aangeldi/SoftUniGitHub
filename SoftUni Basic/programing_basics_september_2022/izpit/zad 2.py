shirts_price = float(input())
sum = float(input())
discoutn = 0.15

shorts_price = shirts_price * 0.75
socks_price = shorts_price * 0.20
boots_price = 2 * (shorts_price + shirts_price)
total = shirts_price + shorts_price + socks_price + boots_price
total = total - total*discoutn
diff = 0
if total >= sum:
    print(f"Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total:.2f} lv.")
else:
    diff = abs(total - sum)
    print(f"No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff:.2f} lv. more.")