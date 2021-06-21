from collections import deque

males = deque(map(int, input().split(" ")))
females = deque(map(int, input().split(" ")))
matches_count = 0

while males and females:
    male, female = males.pop(), females.popleft()
    if male <= 0:
        females.appendleft(female)
        continue
    if female <= 0:
        males.append(male)
        continue
    if male % 25 == 0:
        try:
            males.pop()
        except IndexError:
            pass
        females.appendleft(female)
        continue
    if female % 25 == 0:
        try:
            females.popleft()
        except IndexError:
            pass
        males.append(male)
        continue
    if male == female:
        matches_count += 1
    else:
        if male - 2 > 0:
            males.append(male - 2)

print(f"Matches: {matches_count}")
if males:
    print(f"Males left: {', '.join(reversed(list(map(str, males))))}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join(map(str, females))}")
else:
    print("Females left: none")
