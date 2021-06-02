def valid_coordinates(r, c, n):
    return 0 <= r < n and 0 <= c < n


matrix = [[int(num) for num in input().split()] for _ in range(int(input()))]

commands = input()
while not commands == "END":
    action, row, column, value = commands.split()
    row, column, value = int(row), int(column), int(value)

    if action == "Add" and valid_coordinates(row, column, len(matrix)):
        matrix[row][column] += value
    elif action == "Subtract" and valid_coordinates(row, column, len(matrix)):
        matrix[row][column] -= value
    else:
        print("Invalid coordinates")

    commands = input()

print(*[" ".join([str(x) for x in row]) for row in matrix], sep="\n")
