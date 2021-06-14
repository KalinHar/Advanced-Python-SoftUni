from collections import deque


def is_perfect():
    if cherry_b >= 3 and datura_b >= 3 and smoke_b >= 3:
        return True


b_effects = deque(map(int, input().split(', ')))
b_casings = deque(map(int, input().split(', ')))
cherry_b = 0
datura_b = 0
smoke_b = 0

while b_effects and b_casings:
    effect = b_effects.popleft()
    casing = b_casings.pop()
    sum_values = effect + casing

    if sum_values == 60:
        cherry_b += 1
        if is_perfect():
            break
    elif sum_values == 40:
        datura_b += 1
        if is_perfect():
            break
    elif sum_values == 120:
        smoke_b += 1
        if is_perfect():
            break
    else:
        b_effects.appendleft(effect)
        b_casings.append(casing - 5)

if is_perfect():
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if b_effects:
    print(f"Bomb Effects: {', '.join(map(str, b_effects))}")
else:
    print("Bomb Effects: empty")
if b_casings:
    print(f"Bomb Casings: {', '.join(map(str, b_casings))}")
else:
    print("Bomb Casings: empty")
print(f"Cherry Bombs: {cherry_b}")
print(f"Datura Bombs: {datura_b}")
print(f"Smoke Decoy Bombs: {smoke_b}")
