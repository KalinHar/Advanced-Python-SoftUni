quantity_of_water = int(input())
names = []

while True:
    name = input()
    if name == "Start":
        break
    names.append(name)

command = input()
while command != "End":
    if "refill" in command:
        com, add_liters = command.split()
        quantity_of_water += int(add_liters)
    else:
        if quantity_of_water >= int(command):
            quantity_of_water -= int(command)
            print(f"{names.pop(0)} got water")
        else:
            print(f"{names.pop(0)} must wait")
    command = input()
print(f"{quantity_of_water} liters left")
