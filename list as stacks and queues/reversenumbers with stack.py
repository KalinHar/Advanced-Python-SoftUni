# numbers = [int(x) for x in input().split(" ")]
numbers = input().split()
reversed_numbers = []
while numbers:
    reversed_numbers.append(numbers.pop())
print(*reversed_numbers, sep=" ")
