n = int(input())

matrix = []

for r in range(n):
    line = list(input())
    matrix.append(line)

symb = input()
result = []
for r in range(n):
    for c in range(n):
        if matrix[r][c] == symb:
            result.append([r, c])

if result:
    print(f"({result[0][0]}, {result[0][1]})")
else:
    print(f"{symb} does not occur in the matrix")
