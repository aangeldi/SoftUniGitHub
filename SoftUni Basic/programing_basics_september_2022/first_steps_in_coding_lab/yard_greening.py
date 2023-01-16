kv_m_price = 7.61
discount = 0.18
area = float(input())
price = float(area * kv_m_price)
discount_price = float(price * discount)
total_price = float(price - discount_price)

print(f"The final price is: {total_price} lv.")
print(f"The discount is: {discount_price} lv.")