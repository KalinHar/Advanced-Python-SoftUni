def swap_matrix():
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    for line in matrix:
        print(" ".join(line))


rows, columns = (int(x) for x in input().split())

matrix = []
for _ in range(rows):
    matrix.append([x for x in input().split(" ")])

command = input()
while command != "END":
    try:
        swap, row1, col1, row2, col2 = command.split()
        row1 = int(row1)
        col1 = int(col1)
        row2 = int(row2)
        col2 = int(col2)
    except:
        print("Invalid input!")
        command = input()
        continue
    if swap == "swap" and row1 in range(rows) and row2 in range(rows) \
                        and col1 in range(columns) and col2 in range(columns):
        swap_matrix()
    else:
        print("Invalid input!")
    command = input()
