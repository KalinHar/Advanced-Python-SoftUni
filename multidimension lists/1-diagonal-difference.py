def get_matrix(rows):
    matrix = []
    for _ in range(rows):
        matrix.append([int(x) for x in input().split(" ")])
    return matrix


n = int(input())
m_trix = get_matrix(n)

sum_right_down = 0
for i in range(n):
    sum_right_down += m_trix[i][i]

sum_right_up = 0
for i in range(n):
    sum_right_up += m_trix[i][n - 1 - i]

print(abs(sum_right_down - sum_right_up))


# n = int(input())
# matrix = []
# diagonal1 = 0
# diagonal2 = 0
# for _ in range(n):
#     row = [int(x) for x in input().split()]
#     matrix.append(row)
# for index in range(n):
#     diagonal1 += matrix[index][index]
#     diagonal2 += matrix[index][~index]
# print(f"{abs(diagonal1-diagonal2)}")