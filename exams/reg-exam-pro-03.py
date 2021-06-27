def math_operations(*numbers, **operations):
    from collections import deque
    action = deque([k for k in operations])
    nums = deque(numbers)
    while nums:
        num = nums.popleft()
        act = action.popleft()
        if act == "a":
            operations[act] += num
        elif act == "s":
            operations[act] -= num
        elif act == "d":
            try:
                operations[act] /= num
            except ZeroDivisionError:
                pass
        elif act == "m":
            operations[act] *= num
        action.append(act)
    return operations


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))
