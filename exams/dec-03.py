# def get_magic_triangle(n):
#     triangle = [[1], [1, 1]]
#     for r in range(1, n - 1):
#         row = triangle[r]
#         line = [1]
#         for i in range(len(row) - 1):
#             line.append(sum(row[i: i + 2]))
#         line.append(1)
#         triangle.append(line)
#     return triangle
#

def get_magic_triangle(rows):
    row = [1]
    triangle = [[1]]
    for i in range(rows - 1):
        row = [sum(x) for x in zip([0] + row, row + [0])]
        triangle.append(row)
    return triangle


print(get_magic_triangle(3))
