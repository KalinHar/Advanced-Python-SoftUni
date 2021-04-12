command = input()
queue = []
while command != "End":
    if command != "Paid":
        queue.append(command)
    else:
        while queue:
            print(queue.pop(0))
    command = input()
print(f"{len(queue)} people remaining.")
