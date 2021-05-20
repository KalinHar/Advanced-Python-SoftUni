from collections import deque

command = input()
queue = deque()

while command != "End":
    if command != "Paid":
        queue.append(command)
    else:
        while queue:
            print(queue.popleft())  # .popright() as stack
    command = input()
print(f"{len(queue)} people remaining.")
