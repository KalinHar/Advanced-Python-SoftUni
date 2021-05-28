def get_matrix(rows):
    matrix =[]
    for _ in range(rows):
        matrix.append([x for x in input().split(" ")])
    return matrix


def find_2x2(r_start, c_start):
    for r in range(2):
        for c in range(2):
            char = matrix[r_start + r][c_start + c]
            bunker.add(char)
    if len(bunker) == 1:
        return 1
    else:
        return 0


counter = 0
bunker = set()
rows, columns = (int(x) for x in input().split(" "))

matrix = get_matrix(rows)

for r in range(rows-1):
    for c in range(columns-1):
        counter += find_2x2(r, c)
        bunker = set()

print(counter)
