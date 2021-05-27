n = int(input())
longest_inter = set()

for _ in range(n):
    first, second = input().split("-")
    start_first, end_first = first.split(",")
    start_second, end_second = second.split(",")
    first_iter = set(range(int(start_first), int(end_first) + 1))
    second_iter = set(range(int(start_second), int(end_second) + 1))
    if len(first_iter.intersection(second_iter)) > len(longest_inter):
        longest_inter = first_iter.intersection(second_iter)

print(f"Longest intersection is {list(sorted(longest_inter))} with length {len(longest_inter)}")
