def check_for_king(kings):
    m_king = tuple()
    max_hit_kings = 0
    for king in kings:
        hits_kings = 0
        for pole in hit_poles:
            hit_pole = (king[0] + pole[0], king[1] + pole[1])
            if hit_pole in kings:
                hits_kings += 1
        if hits_kings > max_hit_kings:
            max_hit_kings = hits_kings
            m_king = king
    return m_king


n_board = int(input())
kings = []
for r in range(n_board):
    line = input()
    for c in range(len(line)):
        if line[c] == "K":
            kings.append((r, c))

killed_kings = 0
hit_poles = [(-2, -1), (-2, 1), (2, -1), (2, 1),
            (1, -2), (1, 2), (-1, -2), (-1, 2)]

while True:
    max_king = check_for_king(kings)
    if max_king:
        kings.remove(max_king)
        killed_kings += 1
    else:
        break

print(killed_kings)


# def is_valid(matrix, pot_row, pot_col):
#     return 0 <= pot_row < len(matrix) and 0 <= pot_col < len(matrix)
#
#
# def get_kills(matrix, row, col):
#     kills = 0
#     for index in range(len(rows)):
#         potential_row = row + rows[index]
#         potential_col = col + cols[index]
#         if is_valid(matrix, potential_row, potential_col):
#             potential_position = matrix[potential_row][potential_col]
#             if potential_position == "K":
#                 kills += 1
#     return kills
#
#
# def position_and_max_kills(matrix):
#     max_kills = 0
#     killer_position = []
#     for row_index in range(len(matrix)):
#         for col_index in range(len(matrix)):
#             if matrix[row_index][col_index] == "K":
#                 kills = get_kills(matrix, row_index, col_index)
#                 if kills > max_kills:
#                     max_kills = kills
#                     killer_position = [row_index, col_index]
#     return max_kills, killer_position
#
#
# matrix = [list(input()) for _ in range(int(input()))]
# remove_count = 0
# rows = [-2, -2, 2, 2, 1, 1, -1, -1]
# cols = [-1, 1, -1, 1, -2, 2, -2, 2]
# while True:
#     killings, position = position_and_max_kills(matrix)
#     if position:
#         matrix[position[0]][position[1]] = "0"
#         remove_count += 1
#     else:
#         break
# print(remove_count)