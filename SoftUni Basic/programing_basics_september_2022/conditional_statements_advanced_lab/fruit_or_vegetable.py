fruit_or_vegetable = str(input())
fruit_list = ['banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes']
vegetable_list = ['tomato', 'cucumber', 'pepper', 'carrot']

if fruit_or_vegetable in fruit_list:
    print('fruit')
elif fruit_or_vegetable in vegetable_list:
    print('vegetable')
else:
    print('unknown')