def num_of_player(t):
    if t % 2:
        return 1
    return 2


def get_turn(t, free_r):
    player = num_of_player(t)
    while True:
        print(f"Player {player}, please choose a column.")
        column_num = int(input()) - 1
        if column_num in range(r) and free_r[column_num] >= 0:
            return free_r[column_num], column_num, player
        print("Invalid column index!")


def push_mark(i, j, num):
    global game_board
    game_board[i][j] = num


def print_board():
    [print(row) for row in game_board]


def check_for_winner():
    pass


r, c = [int(x) for x in input().split()]
game_board = [[0 for col in range(c)] for row in range(r)]
free_rows_in_column = [r-1 for _ in range(c)]
turns = 1

while True:
    row, col, mark = get_turn(turns, free_rows_in_column)
    free_rows_in_column[col] -= 1
    push_mark(row, col, mark)
    print_board()
    if turns == r * c:
        print("No winner!")
        print_board()
        break
    turns += 1
