hour = int(input())
day = str(input())
working_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

if hour >= 10 and hour <= 18 and day in working_days:
    print('open')
else:
    print('closed')
