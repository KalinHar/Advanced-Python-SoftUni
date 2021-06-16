from checks import num_of_player


def push_mark(i, j, num, game_board):
    game_board[i][j] = num


def get_turn(turn, free_r_in_c, rows):
    player = num_of_player(turn)
    while True:
        print(f"Player {player}, please choose a column.")
        number_of_column = input()
        if number_of_column.isnumeric():
            number_of_column = int(number_of_column) - 1
            if  number_of_column in range(rows) \
                    and free_r_in_c[number_of_column] >= 0:
                return free_r_in_c[number_of_column], number_of_column, player
        print("Invalid column index!")

