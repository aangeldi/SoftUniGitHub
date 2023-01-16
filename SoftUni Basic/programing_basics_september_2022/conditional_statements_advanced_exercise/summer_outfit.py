degrees = int(input())
day_time = str(input())

if 10 <= degrees <= 18:
    if day_time == 'Morning':
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
    elif day_time == 'Afternoon':
        outfit = 'Shirt'
        shoes = 'Moccasins'
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
    elif day_time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
elif 18 < degrees <= 24:
    if day_time == 'Morning':
        outfit = 'Shirt'
        shoes = 'Moccasins'
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
    elif day_time == 'Afternoon':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
    elif day_time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
elif degrees >= 25:
    if day_time == 'Morning':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
    elif day_time == 'Afternoon':
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
    elif day_time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")