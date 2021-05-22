from collections import deque
liters = deque()
kms = deque()
n = int(input())

for _ in range(n):
    li, k = input().split()
    liters.append(int(li))
    kms.append(int(k))

position = 0
for _ in range(n):
    total_liters = 0
    for i in range(n):
        total_liters += liters[i]
        if total_liters < kms[i]:
            break
        total_liters -= kms[i]

    if i == len(liters) - 1:  # check for full circle
        print(position)
        break

    liters.rotate(-1)
    kms.rotate(-1)
    position += 1
