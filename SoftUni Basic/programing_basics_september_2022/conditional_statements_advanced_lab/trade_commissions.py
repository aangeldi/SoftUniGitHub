city = str(input())
sales = float(input())
city_list = ['Sofia', 'Varna', 'Plovdiv']

if city in city_list and sales >=0:
    if city == 'Sofia':
        if 0 <= sales <= 500:
            commission = sales * 0.05
        elif 500 < sales <= 1000:
            commission = sales * 0.07
        elif 1000 < sales <= 10000:
            commission = sales * 0.08
        elif 1000 < sales:
            commission = sales * 0.12
        print(f'{commission:.2f}')
    if city == 'Varna':
        if 0 <= sales <= 500:
            commission = sales * 0.045
        elif 500 < sales <= 1000:
            commission = sales * 0.075
        elif 1000 < sales <= 10000:
            commission = sales * 0.10
        elif 1000 < sales:
            commission = sales * 0.13
        print(f'{commission:.2f}')
    if city == 'Plovdiv':
        if 0 <= sales <= 500:
            commission = sales * 0.055
        elif 500 < sales <= 1000:
            commission = sales * 0.08
        elif 1000 < sales <= 10000:
            commission = sales * 0.12
        elif 1000 < sales:
            commission = sales * 0.145
        print(f'{commission:.2f}')
else:
    print('error')