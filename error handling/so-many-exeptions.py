# numbers_list = [int(x) for x in input().split(', ')]
# result = 1
#
# for number in numbers_list:
#     if number <= 5:
#         result *= number
#     elif number > 5:
#         result /= number
#
# print(result)

from errors import ValueCannotBeNegative

for _ in range(5):
    num = int(input())
    if num < 0:
        raise ValueCannotBeNegative
