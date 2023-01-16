budget = float(input())
cards = int(input())
processors = int(input())
memory = int(input())

card_price = 250 * cards
processor_price = (0.35 * card_price) * processors
memory_price = (0.1 * card_price) * memory
sum = card_price + processor_price + memory_price

if cards > processors:
    discount = 0.15 * sum
    sum = sum - discount
if budget >= sum:
    left = budget - sum
    print (f"You have {left:.2f} leva left!")
else:
    left = sum - budget
    print(f"Not enough money! You need {left:.2f} leva more!")