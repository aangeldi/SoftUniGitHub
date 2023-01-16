mounts = input()
nights = int(input())
total_apartment=0
total_studio=0

if mounts == "May" or mounts == "October":
    studio = 50
    apartment = 65
    total_studio = studio*nights
    total_apartment = apartment*nights
    if nights > 14:
        studio = studio - studio * 0.30
        total_studio = studio * nights
        apartment = apartment - apartment * 0.10
        total_apartment = apartment * nights
    elif nights > 7:
        studio = studio - studio*0.05
        total_studio = studio * nights
elif mounts == "June" or mounts == "September":
    studio = 75.20
    apartment = 68.70
    total_studio = studio * nights
    total_apartment = apartment * nights
    if nights > 14:
        studio = studio - studio * 0.20
        total_studio = studio * nights
        apartment = apartment - apartment * 0.10
        total_apartment = apartment * nights
elif mounts == "July" or mounts == "August":
    studio = 76
    apartment = 77
    total_studio = studio * nights
    total_apartment = apartment * nights
    if nights > 14:
        apartment = apartment - apartment * 0.10
        total_apartment = apartment * nights

print(f"Apartment: {total_apartment:.2f} lv.")
print(f"Studio: {total_studio:.2f} lv.")
