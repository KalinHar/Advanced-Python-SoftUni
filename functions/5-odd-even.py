def condition(command):
    if command == "Odd":
        return lambda x: x % 2 != 0
    else:
        return lambda x: x % 2 == 0


command = input()
nums = list(map(int, input().split()))

print(sum(filter(condition(command), nums)) * len(nums))
