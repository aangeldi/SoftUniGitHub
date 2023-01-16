flower_type = str(input())
flower_quantity = int(input())
budget = int(input())
roses_price = 5.00
dahlias_price = 3.80
tulips_price = 2.80
narcissus_price = 3.00
gladiolus_price = 2.50
sum = 0

if flower_type == 'Roses':
    sum = flower_quantity * roses_price
    if flower_quantity > 80:
        discount = sum * 0.1
        sum = sum -discount
elif flower_type == 'Dahlias':
    sum = flower_quantity * dahlias_price
    if flower_quantity > 90:
        discount = sum * 0.15
        sum = sum - discount
elif flower_type == 'Tulips':
    sum = flower_quantity * tulips_price
    if flower_quantity > 80:
        discount = sum * 0.15
        sum = sum - discount
elif flower_type == 'Narcissus':
    sum = flower_quantity * narcissus_price
    if flower_quantity < 120:
        discount = sum * 0.15
        sum = sum + discount
elif flower_type == 'Gladiolus':
    sum = flower_quantity * gladiolus_price
    if flower_quantity < 80:
        discount = sum * 0.20
        sum = sum + discount

if budget >= sum:
    left = budget - sum
    print(f"Hey, you have a great garden with {flower_quantity} {flower_type} and {left:.2f} leva left.")
else:
    left = sum - budget
    print(f"Not enough money, you need {left:.2f} leva more.")