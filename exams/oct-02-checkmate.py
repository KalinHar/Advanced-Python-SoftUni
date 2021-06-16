board = []
for r in range(8):
    row = input().split(" ")
    if "K" in row:
        k_row, k_col = r, row.index("K")
    board.append(row)

hit_queens = []
directions = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]

if min(k_row, k_col) < 4:  # maybe without it, if fix range(1, 8)
    k_range = 8 - min(k_row, k_col)
else:
    k_range = max(k_row, k_col)

for i in range(1, k_range):  # range(1, 8)
    lost_dir = []
    for vector in directions:
        v_row, v_col = vector
        pot_row = v_row * i + k_row
        pot_col = v_col * i + k_col
        if pot_row in range(8) and pot_col in range(8) and board[pot_row][pot_col] == "Q":
            hit_queens.append([pot_row, pot_col])
            lost_dir.append([v_row, v_col])
    for lost in lost_dir:
        directions.remove(lost)

if hit_queens:
    print(*hit_queens, sep="\n")
else:
    print("The king is safe!")
