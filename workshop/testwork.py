def num_of_player(t):
    if t % 2:
        return 1
    return 2


def game(t, board):
    player = num_of_player(t)
    columns = f"Player {player}, please"



r, c = [int(x) for x in input().split()]

game_board = [[int(x) for x in list("0" * c)] for _ in range(r)]
print(game_board)
turns = 1