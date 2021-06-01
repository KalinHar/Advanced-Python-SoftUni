matrix = [[int(num) for num in input().split(", ")] for _ in range(int(input()))]
first_diagonal = [matrix[n][n] for n in range(len(matrix))]
second_diagonal = [matrix[n][len(matrix) - 1 - n] for n in range(len(matrix))]
print(f"First diagonal: {', '.join([str(x)  for x in first_diagonal])}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join([str(x)  for x in second_diagonal])}. Sum: {sum(second_diagonal)}")
