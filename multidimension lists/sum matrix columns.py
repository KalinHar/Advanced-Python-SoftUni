rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for row in range(rows):
    lines = [int(x) for x in input().split(" ")]
    matrix.append(lines)

for c in range(cols):
    col_sum = 0
    for r in range(rows):
        col_sum += matrix[r][c]
    print(col_sum)
