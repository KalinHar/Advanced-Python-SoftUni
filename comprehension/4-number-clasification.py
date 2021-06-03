nums = [int(n) for n in input().split(', ')]
result = {'Positive:': [el for el in nums if el >= 0], 'Negative:': [el for el in nums if el < 0], 'Even:': [el for el in nums if el % 2 == 0], 'Odd:': [el for el in nums if el % 2 != 0]}
for k, v in result.items():
    n = ", ".join([str(x) for x in v])
    print(f"{k} {n}")

# positive = []
# negative = []
# [negative.append(x) if x < 0 else positive.append(x) for x in nums]
#
# odd = []
# even = []
# [even.append(x) if x % 2 == 0 else odd.append(x) for x in nums]
