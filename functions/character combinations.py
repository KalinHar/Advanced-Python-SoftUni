# from itertools import permutations
#
# result = (list(permutations(input().split(), int(input()))))
# for x in result:
#     print(*x, sep=', ')


def permutations(names, count, current_names=[]):
    if len(current_names) == count:
        print("".join(current_names))
        return

    for i in range(len(names)):
        current_names.append(names[i])
        permutations(names[:i] + names[i + 1:], count, current_names)
        current_names.pop()


names = list(input())
permutations(names, len(names))
