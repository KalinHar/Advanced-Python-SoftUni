from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = deque([int(x) for x in input().split()])
wasted_water = 0

while bottles and cups:
    cup = cups.popleft()
    bottle = bottles.pop()
    if bottle < cup:
        cup -= bottle
        cups.appendleft(cup)
    else:
        wasted_water += bottle - cup

if bottles:
    print(f"Bottles: {' '.join([str(x) for x in bottles])}")
else:
    print(f"Cups: {' '.join([str(x) for x in cups])}")
print(f"Wasted litters of water: {wasted_water}")
