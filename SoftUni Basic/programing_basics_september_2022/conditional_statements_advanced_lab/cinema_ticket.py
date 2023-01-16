day = str(input())
days_12 = ['Monday', 'Tuesday', 'Friday']
days_14 = ['Wednesday', 'Thursday']
days_16 = ['Saturday', 'Sunday']

if day in days_12:
    print('12')
elif day in days_14:
    print('14')
elif day in days_16:
    print('16')