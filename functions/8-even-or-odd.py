def even_odd(*args):
    nums = list(args)
    command = nums.pop()
    if command == 'even':
        return [x for x in nums if x % 2 == 0]
    return [x for x in nums if x % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
print(even_odd(1, 2, 3, 4, 5, 6, "even"))
