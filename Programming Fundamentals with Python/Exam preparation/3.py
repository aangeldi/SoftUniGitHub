def drive_car(cars, car_name, distance, fuel):
    car = cars[car_name]
    if car['fuel'] < fuel:
        print("Not enough fuel to make that ride")
    else:
        car['mileage'] += distance
        car['fuel'] -= fuel
        print(f"{car_name} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if car['mileage'] >= 100000:
            del cars[car_name]
            print(f"Time to sell the {car_name}!")


def refuel_car(cars, car_name, fuel):
    car = cars[car_name]
    old_fuel = car['fuel']
    car['fuel'] = min(car['fuel'] + fuel, 75)
    print(f"{car_name} refueled with {car['fuel'] - old_fuel} liters.")


def revert_car(cars, car_name, kilometers):
    car = cars[car_name]
    old_mileage = car['mileage']
    car['mileage'] = max(car['mileage'] - kilometers, 10000)
    if car['mileage'] != old_mileage:
        print(f"{car_name} mileage decreased by {old_mileage - car['mileage']} kilometers.")


n = int(input())
cars = {}
for i in range(n):
    car_info = input().split("|")
    car_name = car_info[0]
    mileage = int(car_info[1])
    fuel = int(car_info[2])
    cars[car_name] = {'mileage': mileage, 'fuel': fuel}

while True:
    command = input()
    if command == "Stop":
        break
    command_parts = command.split(" : ")
    if command_parts[0] == "Drive":
        drive_car(cars, command_parts[1], int(command_parts[2]), int(command_parts[3]))
    elif command_parts[0] == "Refuel":
        refuel_car(cars, command_parts[1], int(command_parts[2]))
    elif command_parts[0] == "Revert":
        revert_car(cars, command_parts[1], int(command_parts[2]))

for car_name, car_info in cars.items():
    print(f"{car_name} -> Mileage: {car_info['mileage']} kms, Fuel in the tank: {car_info['fuel']} lt.")
