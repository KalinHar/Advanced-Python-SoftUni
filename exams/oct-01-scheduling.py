from sys import maxsize

numbers = list(map(int, input().split(", ")))
ind = int(input())

cycles = 0
while True:
    min_num = min(numbers)
    if numbers.index(min_num) == ind:
        cycles += min_num
        break
    cycles += min_num
    numbers[numbers.index(min_num)] = maxsize

print(cycles)
