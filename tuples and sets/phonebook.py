contacts = {}
names = []
command = input()

while not command.isdigit():
    name, phone = command.split("-")
    contacts[name] = phone
    command = input()

for _ in range(int(command)):
    names.append(input())

for n in names:
    if n not in contacts:
        print(f"Contact {n} does not exist.")
    else:
        print(f"{n} -> {contacts[n]}")
