def in_board(j, k):
    if 0 <= j < 5 and 0 <= k < 5:
        return True


board, player, shooting_targets = [], [], []
targets = 0
direction = {'left': (0, -1), 'up': (-1, 0), 'right': (0, 1), 'down': (1, 0)}

for row in range(5):
    line = input().split(" ")
    board.append(line)
    for col in range(5):
        if line[col] == "x":
            targets += 1
        elif line[col] == "A":
            player = [row, col]

n = int(input())
for _ in range(n):
    command = input().split(" ")
    r, c = direction[command[1]]
    if command[0] == "shoot":
        pot_r = player[0]
        pot_c = player[1]
        for _ in range(5):
            pot_r += r
            pot_c += c
            if in_board(pot_r, pot_c) and board[pot_r][pot_c] == "x":
                shooting_targets.append([pot_r, pot_c])
                board[pot_r][pot_c] = "."
                break
        if targets == len(shooting_targets):
            break
    elif command[0] == "move":
        steps = int(command[2])
        pot_r = player[0] + r * steps
        pot_c = player[1] + c * steps
        if in_board(pot_r, pot_c) and board[pot_r][pot_c] == ".":
            board[pot_r][pot_c] = "A"
            board[player[0]][player[1]] = "."
            player = [pot_r, pot_c]

if targets == len(shooting_targets):
    print(f"Training completed! All {targets} targets hit.")
else:
    print(f"Training not completed! {targets - len(shooting_targets)} targets left.")
[print(target) for target in shooting_targets]
