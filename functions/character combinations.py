from itertools import permutations

result = (list(permutations(input().split(), int(input()))))
for x in result:
    print(x)
