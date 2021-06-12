def first_triangle(size):
    for row in range(1, size + 2):
        nums = [x for x in range(1, row)]
        if nums:
            print(" ".join(map(str, nums)))


def second_triangle(size):
    for row in range(size, 0, -1):
        nums = [x for x in range(1, row)]
        if nums:
            print(" ".join(map(str, nums)))


def triangle(n):
    first_triangle(n)
    second_triangle(n)