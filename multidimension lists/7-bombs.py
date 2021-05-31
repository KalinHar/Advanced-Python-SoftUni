from collections import deque


def in_matrix(length, row, col):
    return 0 <= row < length and 0 <= col < length


matrix = [[int(num) for num in input().split()] for _ in range(int(input()))]
bombs = deque(b for b in input().split())

hit_positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

while bombs:
    bomb_row, bomb_col = (int(x) for x in bombs.popleft().split(","))
    if matrix[bomb_row][bomb_col] > 0:
        hit_points = matrix[bomb_row][bomb_col]
        matrix[bomb_row][bomb_col] = 0
        for r, c in hit_positions:
            if in_matrix(len(matrix), bomb_row + r, bomb_col + c) \
                    and matrix[bomb_row + r][bomb_col + c] > 0:
                matrix[bomb_row + r][bomb_col + c] -= hit_points

alive_cells_sum = 0
alive_cells_count = 0
for m_row in matrix:
    alive_cells = [cell for cell in m_row if cell > 0]
    alive_cells_sum += sum(alive_cells)
    alive_cells_count += len(alive_cells)

print(f"Alive cells: {alive_cells_count}\nSum: {alive_cells_sum}")
for r in matrix:
    print(*r, sep=" ")
