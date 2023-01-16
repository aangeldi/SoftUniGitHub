deposit = float(input())
term_deposit = int(input())
year_percent = float(input())

sum = (deposit + (term_deposit * ((deposit * year_percent/100)/12)))

print(f"{sum}")

