days = int(input())
players = int(input())
groups_energy = float(input())
water_per_day = float(input())
food_per_day = float(input())
# energy_loss = []
total_water = days * players * water_per_day
total_food = days * players * food_per_day
counter = 0

for i in range(days):
    counter += 1
    energy_loss = float(input())
    groups_energy -= energy_loss
    if groups_energy <= 0:
        print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
        exit(0)

    if counter % 2 == 0:
        groups_energy += 0.05 * groups_energy
        total_water -= 0.3 * total_water
    if counter % 3 == 0:
        groups_energy += 0.1 * groups_energy
        total_food = total_food - (total_food / players)

print(f"You are ready for the quest. You will be left with - {groups_energy:.2f} energy!")

