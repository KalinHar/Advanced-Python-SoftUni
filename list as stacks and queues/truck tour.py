# petrol_pumps = []
#
# n = int(input())
# for _ in range(n):
#     liters, km = input().split()
#     petrol_pumps.append({"liters": int(liters), "km": int(km)})
#
# for i, val in enumerate(petrol_pumps):
#     if val["liters"] >= val["km"]:
#         print(i)
#         break

from collections import deque
liters = deque()
kms = deque()
n = int(input())

for _ in range(n):
    li, km = input().split()
    liters.append(int(li))
    kms.append(int(km))

total_liters = 0
for i in range(n-1):
    total_liters += liters[i]
    if total_liters >= kms[i]:
        total_liters -= kms[i]
