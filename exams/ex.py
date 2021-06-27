def in_range(j, k):
    if 0 <= j < 5 and 0 <= k < 5:
        return True


board = []
player = []
targets = []
shoot = []
direction = {'left': (0, -1), 'up': (-1, 0), 'right': (0, 1), 'down': (1, 0)}

for row in range(5):
    line = input().split(" ")
    board.append(line)
    for i in range(5):
        if line[i] == "x":
            targets.append([row, i])
        elif line[i] == "A":
            player = [row, i]

n = int(input())
for _ in range(n):
    command = input().split(" ")
    if command[0] == "shoot":
        if command[1] == "down":
            for ro in range(player[0], 5):
                if board[ro][player[1]] == "x":
                    shoot.append([ro, player[1]])
                    board[ro][player[1]] = "."
                    break
        elif command[1] == "up":
            for ro in range(player[0], -1, -1):
                if board[ro][player[1]] == "x":
                    shoot.append([ro, player[1]])
                    board[ro][player[1]] = "."
                    break
        elif command[1] == "left":
            for co in range(player[1], -1, -1):
                if board[player[0]][co] == "x":
                    shoot.append([player[0], co])
                    board[player[0]][co] = "."
                    break
        elif command[1] == "right":
            for co in range(player[1], 5):
                if board[player[0]][co] == "x":
                    shoot.append([player[0], co])
                    board[player[0]][co] = "."
                    break
        if len(targets) == len(shoot):
            break
    elif command[0] == "move":
        try:
            r, c = direction[command[1]]
            steps = int(command[2])
        except:
            continue
        pot_r = player[0] + r * steps
        pot_c = player[1] + c * steps
        if in_range(pot_r, pot_c) and board[pot_r][pot_c] == ".":
            board[pot_r][pot_c] = "A"
            board[player[0]][player[1]] = "."
            player = [pot_r, pot_c]
        # for st in range(1, steps + 1):
        #     pot_r = player[0] + r * st
        #     pot_c = player[1] + c * st
        #     if in_range(pot_r, pot_c) and board[pot_r][pot_c] == ".":
        #         if st == steps:
        #             board[pot_r][pot_c] = "A"
        #             board[player[0]][player[1]] = "."
        #             player = [pot_r, pot_c]
        #     else:
        #         break

if len(targets) == len(shoot):
    print(f"Training completed! All {len(targets)} targets hit.")
else:
    print(f"Training not completed! {len(targets) - len(shoot)} targets left.")
[print(el) for el in shoot]
