import re

def calculate_food_info(text):
    pattern = r'(([|#])((?P<name>[\w\s]+))\2(?P<exp>\d{2}\/\d{2}\/\d{2})\2(?P<cal>[0-9]{1,4})\2)'
    total_calories = 0
    food_info = []
    for match in re.finditer(pattern, text):
        name = match.group('name')
        expiration_date = match.group('exp')
        calories = int(match.group('cal'))
        total_calories += calories
        food_info.append({'name': name, 'expiration_date': expiration_date, 'calories': calories})
    return total_calories, food_info,

text = input()
total_calories, food_info = calculate_food_info(text)
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
for food in food_info:
    print(f"Item: {food['name']}, Best before: {food['expiration_date']}, Nutrition: {food['calories']}")
