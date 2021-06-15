def check_player(counter):
    if counter % 2:
        return first_player
    return second_player


def sum_of_4(r, c):
    return sum(map(int, (board[r][0], board[r][-1], board[0][c], board[-1][c])))


first_player, second_player = input().split(', ')
players = {first_player: 501, second_player: 501}
board = [[x for x in input().split(" ")] for _ in range(7)]
count = 0

while True:
    row, col = [int(x) for x in input()[1:-1].split(', ')]  # row, col = eval(input())
    count += 1
    if row not in range(7) or col not in range(7):
        continue
    if board[row][col] == "B":
        break
    elif board[row][col] == "T":
        points = 3 * sum_of_4(row, col)
    elif board[row][col] == "D":
        points = 2 * sum_of_4(row, col)
    else:
        points = int(board[row][col])

    players[check_player(count)] -= points
    if players[check_player(count)] <= 0:
        break

print(f"{check_player(count)} won the game with {(count + 1) // 2} throws!")
