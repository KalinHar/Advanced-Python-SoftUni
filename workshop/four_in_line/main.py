from actions import get_turn, push_mark
from checks import check_for_winner

rows, columns = [int(x) for x in input().split()]
game_board = [[0 for col in range(columns)] for row in range(rows)]
free_row_in_columns = [rows - 1 for _ in range(columns)]
turns = 1

while True:
    row, col, mark = get_turn(turns, free_row_in_columns, rows)
    free_row_in_columns[col] -= 1
    push_mark(row, col, mark, game_board)
    [print(row) for row in game_board]
    winner = check_for_winner(row, col, mark, rows, columns, game_board)
    if winner:
        print(f"The Winner is Player {winner}!")
        break
    if turns == rows * columns:
        print("No winner!")
        break
    turns += 1
