def get_matrix(rows):
    matrix =[]
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
    sum_right_up += m_trix[i][n -1 - i]

print(abs(sum_right_down - sum_right_up))
