def check_player(counter):
    if counter % 2:
        return first_player
    return second_player


first_player, second_player = (n for n in input().split(', '))
board = [[x for x in input().split(" ")] for _ in range(7)]
count = 0
pl_1_points = 501
pl_2_points = 501


while True:
    row, col = eval(input())
    count += 1
    if row not in range(7) or col not in range(7):
        continue
    if board[row][col] == "B":
        break
    elif board[row][col] == "T":
        points = 3 * sum([int(x) for x in [board[row][0], board[row][6], board[0][col], board[6][col]]])
    elif board[row][col] == "D":
        points = 2 * sum([int(x) for x in [board[row][0], board[row][6], board[0][col], board[6][col]]])
    else:
        points = int(board[row][col])
    if count % 2:
        pl_1_points -= points
    else:
        pl_2_points -= points
    if pl_2_points <= 0 or pl_1_points <= 0:
        break

winner = check_player(count)
if winner == first_player:
    count_turns = (count + 1) /2
else:
    count_turns = count / 2

print(f"{winner} won the game with {int(count_turns)} throws!")
