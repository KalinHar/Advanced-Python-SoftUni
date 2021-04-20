n = int(input())
matrix = []

for r in range(n):
    line = [int(x) for x in input().split()]
    matrix.append(line)

diagonal_sum = 0
for i in range(n):
    diagonal_sum += matrix[i][i]

print(diagonal_sum)
