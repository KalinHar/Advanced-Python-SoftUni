kids = input().split()
n = int(input())
k = n - 1

while len(kids) > 1:
    if k >= len(kids):
        k -= len(kids)
    else:
        print(f"Removed {kids.pop(k)}")
        k += (n - 1)

print(f"Last is {kids[0]}")
