rows, cols = [int(x) for x in input().split(", ")]

matrix = []
total_sum = 0

for row in range(rows):
    lines = [int(x) for x in input().split(", ")]
    line_sum = sum(lines)
    total_sum += line_sum
    matrix.append(lines)

print(total_sum)
print(matrix)

