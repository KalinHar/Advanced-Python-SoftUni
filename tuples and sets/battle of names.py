n = int(input())
odd_set = set()
even_set = set()


def name_value(name, row):
    sum_of_char = sum(ord(ch) for ch in name)
    return sum_of_char // row


for i in range(1, n + 1):
    result = name_value(input(), i)
    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

max_odd_sum = sum(odd_set)
max_even_sum = sum(even_set)

if max_even_sum == max_odd_sum:
    print(*odd_set.union(even_set), sep=", ")
elif max_even_sum < max_odd_sum:
    print(*odd_set.difference(even_set), sep=", ")
else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")
