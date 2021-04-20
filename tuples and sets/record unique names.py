def entry_list(n):
    lines = []
    for _ in range(n):
        lines.append(input())
    return lines


count = int(input())
names = entry_list(count)

unique_names = set(names)
for n in unique_names:
    print(n)
