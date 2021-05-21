n = int(input())

sequence = []
for _ in range(n):
    query = input().split()
    if query[0] == "1":
        sequence.append(int(query[1]))
    elif query[0] == "2" and sequence:
        sequence.pop()
    elif query[0] == "3" and sequence:
        print(max(sequence))
    elif query[0] == "4" and sequence:
        print(min(sequence))

reversed_sequence = []
while sequence:
    reversed_sequence.append(sequence.pop())
print(*reversed_sequence, sep=", ")
