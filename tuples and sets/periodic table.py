n = int(input())

elements = set()

for _ in range(n):
    elements = elements.union(set(input().split()))
    # line = input().split()
    # for el in line:
    #     elements.add(el)

print("\n".join(elements))
