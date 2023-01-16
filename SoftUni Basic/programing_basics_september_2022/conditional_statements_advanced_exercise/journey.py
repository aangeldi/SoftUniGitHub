budget = float(input())
season = str(input())

if season == "summer":
    hotel = "Camp"
    if budget <= 100:
        rent = budget * 0.30
        print(f"Somewhere in Bulgaria")
        print(f"{hotel} - {rent:.2f}")
    elif 100 < budget <= 1000:
        rent = budget * 0.40
        print(f"Somewhere in Balkans")
        print(f"{hotel} - {rent:.2f}")
    elif budget > 1000:
        hotel = "Hotel"
        rent = budget * 0.90
        print(f"Somewhere in Europe")
        print(f"{hotel} - {rent:.2f}")
elif season == "winter":
    hotel = "Hotel"
    if budget <= 100:
        rent = budget * 0.70
        print(f"Somewhere in Bulgaria")
        print(f"{hotel} - {rent:.2f}")
    elif 100 < budget <= 1000:
        rent = budget * 0.80
        print(f"Somewhere in Balkans")
        print(f"{hotel} - {rent:.2f}")
    elif budget > 1000:
        rent = budget * 0.90
        print(f"Somewhere in Europe")
        print(f"{hotel} - {rent:.2f}")