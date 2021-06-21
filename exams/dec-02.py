from collections import deque


def move(row_col):
    global board, player, text

    row, col = row_col
    pl_row, pl_col = player
    n_row, n_col = pl_row + row, pl_col + col
    if n_row not in range(size) or n_col not in range(size):
        text.pop()                        # remove last element from text
        return
    if board[n_row][n_col] != "-":
        text.append(board[n_row][n_col])  # add element at position on board to text
    board[pl_row][pl_col] = "-"           # replace "P"layer position with "-" on board
    board[n_row][n_col] = "P"             # replace new position with "P"layer ob  board
    player = (n_row, n_col)               # player get new position-(row, column)


direction = {'left': (0, -1), 'up': (-1, 0), 'right': (0, 1), 'down': (1, 0)}
board = []

text = deque(input())
size = int(input())
for r in range(size):  # read board and player get position-(row, column)
    line = list(input())
    if "P" in line:
        player = (r, line.index("P"))
    board.append(line)

m = int(input())
for _ in range(m):
    command = input()
    move(direction.get(command))  # move to position of command

print("".join(text))
[print(*r, sep='') for r in board]
