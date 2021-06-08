def is_index_valid(r, c):
    return 0 <= r < n and 0 <= c < n


def check_neighbors(matrix, row, col, directions):
    for direction in directions:
        potential_row, potential_col = row + direction[0], col + direction[1]
        if is_index_valid(potential_row, potential_col):
            if matrix[potential_row][potential_col] != '*':
                matrix[potential_row][potential_col] += 1


n = int(input())
n_bombs = int(input())
matrix = []
bombs_positions = []
directions = [
    [0, -1],  # left
    [-1, -1],  # left up diagonal
    [-1, 0],  # up
    [-1, 1],  # up right diagonal
    [0, 1],  # right
    [1, 1],  # down right diagonal
    [1, 0],  # down
    [1, -1],  # down left diagonal
]

for row in range(n):
    matrix.append([])
    for col in range(n):
        matrix[row].append(0)

for bomb in range(n_bombs):
    row, col = eval(input())
    if is_index_valid(row, col):
        bombs_positions.append([row, col])
        matrix[row][col] = '*'

for bomb in bombs_positions:
    check_neighbors(matrix, bomb[0], bomb[1], directions)

for row in matrix:
    print(*row, sep=' ')
