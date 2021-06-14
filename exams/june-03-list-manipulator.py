def list_manipulator(nums, *commands):
    com_1, com_2, *num = commands
    if com_1 == "add":
        if com_2 == "beginning":
            return num + nums
        elif com_2 == "end":
            return nums + num
    elif com_1 == "remove":
        if com_2 == "beginning":
            if num:
                return nums[num[0]:]
            else:
                return nums[1:]
        elif com_2 == "end":
            if num:
                return nums[: - num[0]]
            else:
                return nums[: -1]


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
