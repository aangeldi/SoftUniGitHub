fruit = str(input())
day = str(input())
quantity = float(input())

fruit_list = ['banana', 'apple', 'orange', 'grapefruit', 'kiwi', 'pineapple', 'grapes']
fruit_price_working_days = [2.50, 1.20, 0.85, 1.45, 2.70, 5.50, 3.85]
day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
fruit_price_weekend = [2.70, 1.25, 0.90, 1.60, 3.00, 5.60, 4.20]
weekend_list = ['Saturday', 'Sunday']

if fruit in fruit_list and (day in day_list or day in weekend_list):
    if fruit == fruit_list[0]:
        if day in day_list :
            price = fruit_price_working_days[0] * quantity
        else:
            price = fruit_price_weekend[0] * quantity
        print(f'{price:.2f}')
    elif fruit == fruit_list[1]:
        if day in day_list :
            price = fruit_price_working_days[1] * quantity
        else:
            price = fruit_price_weekend[1] * quantity
        print(f'{price:.2f}')
    elif fruit == fruit_list[2]:
        if day in day_list :
            price = fruit_price_working_days[2] * quantity
        else:
            price = fruit_price_weekend[2] * quantity
        print(f'{price:.2f}')
    elif fruit == fruit_list[3]:
        if day in day_list :
            price = fruit_price_working_days[3] * quantity
        else:
            price = fruit_price_weekend[3] * quantity
        print(f'{price:.2f}')
    elif fruit == fruit_list[4]:
        if day in day_list :
            price = fruit_price_working_days[4] * quantity
        else:
            price = fruit_price_weekend[4] * quantity
        print(f'{price:.2f}')
    elif fruit == fruit_list[5]:
        if day in day_list :
            price = fruit_price_working_days[5] * quantity
        else:
            price = fruit_price_weekend[5] * quantity
        print(f'{price:.2f}')
    elif fruit == fruit_list[6]:
        if day in day_list :
            price = fruit_price_working_days[6] * quantity
        else:
            price = fruit_price_weekend[6] * quantity
        print(f'{price:.2f}')
else:
    print('error')