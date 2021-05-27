contacts = {}
command = input()

while not command.isnumeric():
    name, phone = command.split("-")
    contacts[name] = phone
    command = input()

for _ in range(int(command)):
    n = input()
    if n not in contacts:
        print(f"Contact {n} does not exist.")
    else:
        print(f"{n} -> {contacts[n]}")
