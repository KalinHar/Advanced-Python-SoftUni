def entry_list(n):
    lines = []
    for _ in range(n):
        lines.append(input())
    return lines


count = int(input())
reservations = entry_list(count)

guests = set('')
command = input()
while command != 'END':
    guests.add(command)
    command = input()

un_come_guests = set(reservations).difference(guests)
print(len(un_come_guests))
for g in sorted(un_come_guests):
    print(g)
