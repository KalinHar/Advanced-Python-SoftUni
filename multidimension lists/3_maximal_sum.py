from sys import maxsize


def get_matrix(rows):
    return [[int(row) for row in input().split()] for _ in range(rows)]


# def sum_3x3(r_start, c_start):
#     matrix_sum = 0
#     m_trix = [[0,0,0],[0,0,0],[0,0,0]]
#     for r in range(3):
#         for c in range(3):
#             num = matrix[r_start + r][c_start + c]
#             m_trix[r][c] = num
#             matrix_sum += num
#     return matrix_sum, m_trix


def sum_3x3(i, j):
    matrix_sum = 0
    m_trix = [
        [matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]],
        [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]],
        [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]
    ]
    for row in m_trix:
        matrix_sum += sum(row)
    return matrix_sum, m_trix


counter = 0
max_sum = -maxsize
max_matrix = []

rows, columns = list(map(int, input().split(" ")))

matrix = get_matrix(rows)

for r in range(rows - 2):
    for c in range(columns - 2):
        result, m_matrix = sum_3x3(r, c)
        if max_sum < result:
            max_sum = result
            max_matrix = m_matrix

print(f"Sum = {max_sum}")
for line in max_matrix:
    print(*line, sep=" ")


# rows, columns = list(map(int, input().split(" ")))
#
# matrix = [[int(row) for row in input().split()] for _ in range(rows)]
# matrix_3x3 = []
# for i in range(len(matrix) - 2):
#     row = matrix[i]
#     for j in range(len(row) - 2):
#         max_3x3 = [
#             matrix[i][j], matrix[i][j + 1], matrix[i][j + 2],
#             matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2],
#             matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2],
#         ]
#         matrix_3x3.append(max_3x3)
# max_matrix_3x3 = max(matrix_3x3, key=lambda x: sum(x))
# beginning = 0
# print(f"Sum = {sum(max_matrix_3x3)}")
# for r in range(1, len(max_matrix_3x3) + 1):
#     if r % 3 == 0:
#         print(*max_matrix_3x3[beginning:r])
#         beginning = r
