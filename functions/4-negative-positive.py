negative = []
positive = []

[negative.append(x) if x < 0 else positive.append(x) for x in map(int, input().split())]

print(sum(negative))
print(sum(positive))

if abs(sum(negative)) > sum(positive):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")


# def is_not_negative(num):
#     return num >= 0
#
#
# nums = list(map(int, input().split()))
# positive_1 = list(filter(is_not_negative, nums))
# positive = list(filter(lambda x: x == is_not_negative, nums))
# negative = list(filter(lambda x: x != is_not_negative, nums))
