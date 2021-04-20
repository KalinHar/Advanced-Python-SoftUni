def entry_list(n):
    lines = []
    for _ in range(n):
        lines.append(input())
    return lines


def entry_list_while(key_word):
    result = []
    while True:
        line = input()
        if line == key_word:
            break
        result.append(line)
    return result


count = int(input())
reservations = set(entry_list(count))

guests = set(entry_list_while("END"))

un_come_guests = reservations.difference(guests)
print(len(un_come_guests))
for g in sorted(un_come_guests):
    print(g)
