from collections import deque

rows, columns = list(map(int, input().split(" ")))
snake = input()

index_snake = 0
matrix = []
for row in range(rows):
    line = deque()
    for _ in range(columns):
        if index_snake == len(snake):
            index_snake = 0

        if row % 2 == 0:
            line.append(snake[index_snake])
        else:
            line.appendleft(snake[index_snake])

        index_snake += 1
    # if row % 2 == 0:
    #     for _ in range(columns):
    #         if index_snake == len(snake):
    #             index_snake = 0
    #         line.append(snake[index_snake])
    #         index_snake += 1
    # else:
    #     for _ in range(columns):
    #         if index_snake == len(snake):
    #             index_snake = 0
    #         line.appendleft(snake[index_snake])
    #         index_snake += 1
    matrix.append(line)

for r in matrix:
    print(*r, sep="")
