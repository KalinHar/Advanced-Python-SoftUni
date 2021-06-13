def out_of_maze(r, c):
    return r not in range(n) or c not in range(n)


n = int(input())
maze = []
b_marks = []
snake = []
food_quantity = 0
direction = {'left': (0, -1), 'up': (-1, 0), 'right': (0, 1), 'down': (1, 0)}

for row in range(n):
    line = list(input())
    if "S" in line:
        snake = [row, line.index("S")]
    if "B" in line:
        b_marks.append([row, line.index("B")])
    maze.append(line)

while True:
    [print("".join(row)) for row in maze]
    move = input()
    new_row, new_col = snake[0] + direction[move][0], snake[1] + direction[move][1]
    if out_of_maze(new_row, new_col):
        maze[snake[0]][snake[1]] = "."
        break
    if maze[new_row][new_col] == "*":
        maze[new_row][new_col] = "S"
        maze[snake[0]][snake[1]] = "."
        snake = [new_row, new_col]
        food_quantity += 1
        if food_quantity == 10:
            break
    elif maze[new_row][new_col] == "B":
        maze[new_row][new_col] = "."
        maze[snake[0]][snake[1]] = "."
        b_marks.remove([new_row, new_col])
        snake = [b_marks[0][0], b_marks[0][1]]
        maze[snake[0]][snake[1]] = "S"
    else:
        maze[new_row][new_col] = "S"
        maze[snake[0]][snake[1]] = "."
        snake = [new_row, new_col]

if food_quantity == 10:
    print("You won! You fed the snake.")
else:
    print("Game over!")
print(f"Food eaten: {food_quantity}")
[print("".join(row)) for row in maze]
