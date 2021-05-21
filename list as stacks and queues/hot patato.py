from collections import deque
kids = deque(input().split())
n = int(input())

# kid_to_remove = n - 1
# while len(kids) > 1:
#     if kid_to_remove >= len(kids):
#         kid_to_remove -= len(kids)
#     else:
#         print(f"Removed {kids.pop(kid_to_remove)}")
#         kid_to_remove += (n - 1)
# print(f"Last is {kids.pop()}")

while len(kids) > 1:
    kids.rotate(-n)
    print(f"Removed {kids.pop()}")
print(f"Last is {kids.pop()}")
