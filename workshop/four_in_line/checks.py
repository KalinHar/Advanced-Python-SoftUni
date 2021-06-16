def num_of_player(turn):
    if turn % 2:
        return 1
    return 2


def check_for_winner(i, j, num, rows, columns, game_board):
    winning_lines = [
        [[[+1, -1], [+2, -2], [+3, -3]], [[-1, +1], [-2, +2], [-3, +3]]],  # diagonal: left,down - right,up
        [[[+1, +1], [+2, +2], [+3, +3]], [[-1, -1], [-2, -2], [-3, -3]]],  # diagonal: right,down - left,up
        [[[0, -1], [0, -2], [0, -3]], [[0, +1], [0, +2], [0, +3]]],        # horizontal: left - right
        [[[+1, 0], [+2, 0], [+3, 0]], [[-1, 0], [-2, 0], [-3, 0]]],        # vertical: down - !(up)
    ]
    for line in winning_lines:
        four_in_line = 1
        for half_line in line:
            for row_col in half_line:
                n_row, n_col = i + row_col[0], j + row_col[1]
                if n_row in range(rows) and n_col in range(columns) and game_board[n_row][n_col] == num:
                    four_in_line += 1
                    if four_in_line == 4:
                        return num
                else:
                    break
