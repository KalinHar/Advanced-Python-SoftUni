def start_end_list(start, end):
    return [x for x in range(start, end + 1)]


def div_numbers(n):
    return any(n % x == 0 for x in nums_to_ten)


def filter_nums(n):
    return [x for x in n if div_numbers(x)]


st = int(input())
ed = int(input())
nums_to_ten = [x for x in range(2, 11)]
nums = start_end_list(st, ed)
print(filter_nums(nums))
