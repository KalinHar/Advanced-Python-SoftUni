def palindromes(r, c):
    # base = ord('a')
    # first_letter = chr(base + r)
    # second_letter = chr((base + r + c)
    # return first_letter + second_letter + first_letter
    return chr(97 + r) + chr(97 + c + r) + chr(97 + r)


rows, cols = [int(x) for x in input().split()]
matrix = [[palindromes(r, c) for c in range(cols)] for r in range(rows)]

[print(' '.join(row)) for row in matrix]
