nums = [int(n) for n in input().split(', ')]
result = {'Positive:': [el for el in nums if el >= 0], 'Negative:': [el for el in nums if el < 0], 'Even:': [el for el in nums if el % 2 == 0], 'Odd:': [el for el in nums if el % 2 != 0]}
for k, v in result.items():
    n = ", ".join([str(x) for x in v])
    print(f"{k} {n}")
