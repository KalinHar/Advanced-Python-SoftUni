def num_of_player(t):
    if t % 2:
        return 1
    return 2


def get_turn(t, free_r,):
    player = num_of_player(t)
    while True:
        print(f"Player {player}, please choose a column.")
        column = int(input()) - 1
        if column in range(r) and free_r[column] >= 0:



r, c = [int(x) for x in input().split()]

game_board = [[int(x) for x in list("0" * c)] for _ in range(r)]
free_rows_in_column = [r-1 for _ in range(c)]
turns = 1