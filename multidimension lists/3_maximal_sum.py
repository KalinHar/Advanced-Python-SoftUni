from sys import maxsize


def get_matrix(rows):
    matrix =[]
    for _ in range(rows):
        matrix.append([int(x) for x in input().split(" ")])
    return matrix


def sum_3x3(r_start, c_start):
    matrix_sum = 0
    m_trix = [[0,0,0],[0,0,0],[0,0,0]]
    for r in range(3):
        for c in range(3):
            num = matrix[r_start + r][c_start + c]
            m_trix[r][c] = num
            matrix_sum += num
    return matrix_sum, m_trix


counter = 0
max_sum = -maxsize
max_matrix = []

rows, columns = (int(x) for x in input().split(" "))

matrix = get_matrix(rows)

for r in range(rows-2):
    for c in range(columns-2):
        result, m_matrix = sum_3x3(r, c)
        if max_sum < result:
            max_sum = result
            max_matrix = m_matrix

print(f"Sum = {max_sum}")
for line in max_matrix:
    print(*line,sep=" ")
