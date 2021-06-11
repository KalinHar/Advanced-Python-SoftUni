def index_is_out(r, c):
    return r not in range(n) or c not in range(n)


n = int(input())
matrix = []
for row in range(n):
    m_row = list(input().split(' '))  # read the matrix
    if "P" in m_row:                  # and player position
        col = m_row.index("P")
        player = (row, col)
        m_row[col] = 0
    matrix.append(m_row)

coins = 0
player_path = []
direction = {'left': (0, -1), 'up': (-1, 0), 'right': (0, 1), 'down': (1, 0)}

while True:
    move = input()
    new_row, new_col = player[0] + direction[move][0], player[1] + direction[move][1]
    if index_is_out(new_row, new_col) or matrix[new_row][new_col] == 'X':
        coins = coins // 2
        break
    player = (new_row, new_col)
    player_path.append([new_row, new_col])
    coins += int(matrix[new_row][new_col])
    matrix[new_row][new_col] = 0
    if coins >= 100:
        break

if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")
print("Your path:")
print(*player_path, sep="\n")
