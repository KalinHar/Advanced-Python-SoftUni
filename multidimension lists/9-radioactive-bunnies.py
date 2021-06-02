def in_matrix(r, c):
    return 0 <= r < rows and 0 <= c < cols


def move(r, c, direct):
    dif_r, dif_c = directions[direct]
    new_r, new_c = r + dif_r, c + dif_c
    if in_matrix(new_r, new_c):
        return new_r, new_c
    return None


def move_bunnies():
    global win, bunnies
    new_bunnies = []
    while bunnies:
        bunny_r, bunny_c = bunnies.pop()
        for d in directions:
            bunny = move(bunny_r, bunny_c, d)
            if bunny:
                if matrix[bunny[0]][bunny[1]] == ".":
                    matrix[bunny[0]][bunny[1]] = "B"
                    new_bunnies.append((bunny[0], bunny[1]))
                elif matrix[bunny[0]][bunny[1]] == "P":
                    win = False
                    matrix[bunny[0]][bunny[1]] = "B"
                    new_bunnies.append((bunny[0], bunny[1]))
    bunnies = new_bunnies


rows, cols = [int(x) for x in input().split()]
directions = {
    "U": (-1, 0),
    "R": (0, +1),
    "D": (+1, 0),
    "L": (0, -1)
}
bunnies = []
win = True
# matrix = [[char for char in list(input())] for _ in range(rows)]
matrix = []
for i in range(rows):
    matrix.append([])
    row = input()
    for j in range(cols):
        matrix[i].append(row[j])
        if row[j] == "P":
            player = (i, j)
        elif row[j] == "B":
            bunnies.append((i, j))

commands = input()

for direction in commands:
    player_r, player_c = player
    player = move(player_r, player_c, direction)
    if not player:
        win = True
        matrix[player_r][player_c] = "."
        player = player_r, player_c
        move_bunnies()
        break
    elif matrix[player[0]][player[1]] == "B":
        matrix[player_r][player_c] = "."
        win = False
        move_bunnies()
        break
    else:
        matrix[player[0]][player[1]] = "P"
        matrix[player_r][player_c] = "."
        move_bunnies()
        if not win:
            break

[print("".join(row)) for row in matrix]
if win:
    print(f"won: {' '.join([str(x) for x in player])}")
else:
    print(f"dead: {' '.join([str(x) for x in player])}")
