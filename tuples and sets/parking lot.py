def entry_list(n):
    lines = []
    for _ in range(n):
        lines.append(input())
    return lines


count = int(input())
cars = entry_list(count)

park_cars = set()
for car in cars:
    command, number = car.split(", ")
    if command == "IN":
        park_cars.add(number)
    elif command == "OUT":
        park_cars.discard(number)  # remove without error if not exist

if park_cars:
    print('\n'.join(park_cars))
else:
    print("Parking Lot is Empty")
