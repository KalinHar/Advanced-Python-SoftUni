def best_list_pureness(*numbers):
    from collections import deque
    nums, k_times = numbers
    nums = deque(nums)
    pureness = {}
    for k in range(k_times + 1):
        pure = sum([i*n for i, n in enumerate(nums)])
        if pure not in pureness:
            pureness[pure] = k
        nums.rotate()
    return f"Best pureness {max(pureness)} after {pureness[max(pureness)]} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
