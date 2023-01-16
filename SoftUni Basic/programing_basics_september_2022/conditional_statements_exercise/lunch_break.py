import math

serial_title = str(input())
movie_duration = int(input())
break_duration = int(input())

lunch_duration = break_duration/8
silence_duration = break_duration/4

timing_left = break_duration - (lunch_duration + silence_duration)

if timing_left >= movie_duration:
    left = timing_left - movie_duration
    left = math.ceil(left)
    print (f"You have enough time to watch {serial_title} and left with {left} minutes free time.")
else:
    left = movie_duration - timing_left
    left = math.ceil(left)
    print(f"You don't have enough time to watch {serial_title}, you need {left} more minutes.")