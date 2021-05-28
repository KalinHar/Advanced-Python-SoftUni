n = int(input())
matrix = []

for r in range(n):
    matrix.append([int(x) for x in input().split()])

diagonal_sum = 0
for i in range(n):
    diagonal_sum += matrix[i][i]

print(diagonal_sum)
