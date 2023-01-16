days_stay = int(input()) #[0...365]
room = str(input()) #"room for one person", "apartment" или "president apartment"
evaluation = str(input()) #"positive"  или "negative"
totatl_price = 0
added_value = 0
if room =="room for one person":
    price_per_night = 18.00
    totatl_price = price_per_night*(days_stay-1)
elif room =="apartment":
    price_per_night = 25.00
    totatl_price = price_per_night * (days_stay-1)
    if days_stay < 10:
        discount = totatl_price *0.30
        totatl_price = totatl_price - discount
    elif 10 <= days_stay <= 15:
        discount = totatl_price * 0.35
        totatl_price = totatl_price - discount
    elif days_stay > 15:
        discount = totatl_price * 0.50
        totatl_price = totatl_price - discount
elif room =="president apartment":
    price_per_night = 35.00
    totatl_price = price_per_night * (days_stay - 1)
    if days_stay < 10:
        discount = totatl_price * 0.10
        totatl_price = totatl_price - discount
    elif 10 <= days_stay <= 15:
        discount = totatl_price * 0.15
        totatl_price = totatl_price - discount
    elif days_stay > 15:
        discount = totatl_price * 0.20
        totatl_price = totatl_price - discount

if evaluation == "positive":
    added_value = totatl_price + totatl_price*0.25
elif evaluation == "negative":
    added_value = totatl_price - totatl_price * 0.10
print(f"{added_value:.2f}")
