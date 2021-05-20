from collections import deque

quantity_of_water = int(input())
names = deque()

while True:
    name = input()
    if name == "Start":
        break
    names.append(name)

command = input()
while command != "End":
    if command.startswith("refill"):
        quantity_of_water += int(command.split()[-1])
    else:
        if quantity_of_water >= int(command):
            quantity_of_water -= int(command)
            print(f"{names.popleft()} got water")
        else:
            print(f"{names.popleft()} must wait")
    command = input()
print(f"{quantity_of_water} liters left")
