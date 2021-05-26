n = int(input())
longest_inter = set()


def set_in_range(start, end):
    line = set()
    for i in range(start, end + 1):
        line.add(i)
    return line


for _ in range(n):
    first, second = input().split("-")
    s_first, e_first = first.split(",")
    s_second, e_second = second.split(",")
    first_iter = set_in_range(int(s_first), int(e_first))
    second_iter = set_in_range(int(s_second), int(e_second))
    if len(first_iter.intersection(second_iter)) > len(longest_inter):
        longest_inter = first_iter.intersection(second_iter)

print(f"Longest intersection is {list(sorted(longest_inter))} with length {len(longest_inter)}")
