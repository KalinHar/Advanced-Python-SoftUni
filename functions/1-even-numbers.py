print(list(filter(lambda x: x % 2 == 0, map(int, input().split()))))


def is_even(num):
    return num % 2 == 0


even_nums = list(filter(is_even, [1,2,3,4,5,6]))
