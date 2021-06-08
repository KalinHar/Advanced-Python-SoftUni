def numbers_searching(*numbers):
    min_num = min(numbers)
    max_num = max(numbers)
    missing_num = None
    duplicates = set()
    for i in range(min_num, max_num + 1):
        if i not in numbers:
            missing_num = i
        if numbers.count(i) > 1:
            duplicates.add(i)
    return [missing_num, list(sorted(duplicates))]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
