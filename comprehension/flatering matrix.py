def read_matrix(r):
    result = [input().split(', ') for _ in range(r)]
    return [[int(x) for x in row] for row in result]


def print_matrix(mat):
    print(mat)


def flat_matrix(mat):
    return [x for row in mat for x in row]


matrix = read_matrix(int(input()))
print_matrix(flat_matrix(matrix))
