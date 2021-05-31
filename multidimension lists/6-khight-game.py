def check_for_king(kings):
    m_king = []
    max_hit_kings = 0
    hit_poles = [
        [-2, -1], [-2, 1], [2, -1], [2, 1],
        [1, -2], [1, 2], [-1, -2], [-1, 2]
        ]
    for king in kings:
        hits_kings = 0
        for pole in hit_poles:
            row = king[0] + pole[0]
            col = king[1] + pole[1]
            hit_pole = [row, col]
            if hit_pole in kings:
                hits_kings += 1
        if hits_kings > max_hit_kings:
            max_hit_kings = hits_kings
            m_king = king
    return m_king


n_board = int(input())
kings =[]
for r in range(n_board):
    line = input()
    for c in range(len(line)):
        if line[c] == "K":
            kings.append([r, c])

killed_kings = 0

while True:
    max_king = check_for_king(kings)
    if max_king:
        kings.remove(max_king)
        killed_kings += 1
    else:
        break

print(killed_kings)
