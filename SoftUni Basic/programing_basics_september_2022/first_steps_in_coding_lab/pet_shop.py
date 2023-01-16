dog_food_price = 2.5
cat_food_price = 4

count_dog_pack = int(input())
count_cat_pack = int(input())

sum_dog_pack = count_dog_pack*dog_food_price
sum_cat_pack = count_cat_pack*cat_food_price

total_price = sum_dog_pack+sum_cat_pack

print(f"{total_price} lv.")
