country = input().split(", ")
capital = input().split(", ")

data = {country[idx]: capital[idx] for idx in range(len(country))}

for key, value in data.items():
    print(f"{key} -> {value}")

