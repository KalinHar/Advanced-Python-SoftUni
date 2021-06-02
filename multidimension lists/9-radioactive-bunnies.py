def move(r, c, direct):
    dif_r, dif_c = directions[direct]
    new_r, new_c = r + dif_r, c + dif_c
    if 0 <= new_r < rows and 0 <= new_c < cols:
        return new_r, new_c
    return None


def spread_bunnies():
    global alive, bunnies
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
                    alive = False
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
alive = True

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
        alive = True
        matrix[player_r][player_c] = "."
        player = player_r, player_c
        spread_bunnies()
        break
    elif matrix[player[0]][player[1]] == "B":
        alive = False
        matrix[player_r][player_c] = "."
        spread_bunnies()
        break
    else:
        matrix[player[0]][player[1]] = "P"
        matrix[player_r][player_c] = "."
        spread_bunnies()
        if not alive:
            break

[print("".join(row)) for row in matrix]
if alive:
    print(f"won: {' '.join([str(x) for x in player])}")
else:
    print(f"dead: {' '.join([str(x) for x in player])}")
