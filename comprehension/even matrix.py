def read_matrix(r):
    result = [input().split(', ') for _ in range(r)]
    return [[int(x) for x in row] for row in result]


def print_matrix(mat):
    print(mat)


def evan_matrix(mat):
    return [[x for x in row if x % 2 == 0] for row in mat]


matrix = read_matrix(int(input()))
print_matrix(evan_matrix(matrix))
