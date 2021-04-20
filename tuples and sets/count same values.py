numbers = tuple(map(float, input().split()))
num_counts = {}
for n in numbers:
    if n not in num_counts:
        num_counts[n] = 0
    num_counts[n] += 1
[print(f"{key} - {value} times") for key, value in num_counts.items()]
