import sys

rows, cols = [int(x) for x in input().split(", ")]

matrix = []
for r in range(rows):
    line = [int(x) for x in input().split(", ")]
    matrix.append(line)

max_sum = - sys.maxsize
sub_matrix = []
for r in range(rows - 1):
    for c in range(cols - 1):
        sub_mat_sum = matrix[r][c] + matrix[r][c+1]\
                        + matrix[r+1][c] + matrix[r+1][c+1]
        if sub_mat_sum > max_sum:
            max_sum = sub_mat_sum
            sub_matrix = [[matrix[r][c], matrix[r][c+1]], [matrix[r+1][c], matrix[r+1][c+1]]]

for line in sub_matrix:
    print(" ".join([str(x) for x in line]))
print(max_sum)
