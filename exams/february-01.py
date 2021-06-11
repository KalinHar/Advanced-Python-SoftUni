from collections import deque


def is_perfect():
    if palm_fire >= 3 and willow_fire >= 3 and cross_fire >= 3:
        return True


fire_effect = deque(map(int, input().split(', ')))
expl_power = deque(map(int, input().split(', ')))
palm_fire = 0
willow_fire = 0
cross_fire = 0

while fire_effect and expl_power:
    firework = fire_effect.popleft()
    explosive = expl_power.pop()
    sum_values = firework + explosive

    if explosive <= 0 and firework <= 0:
        continue
    elif explosive <= 0:
        fire_effect.appendleft(firework)
        continue
    elif firework <= 0:
        expl_power.append(explosive)
        continue

    if sum_values % 3 == 0 and sum_values % 5 != 0:
        palm_fire += 1
        if is_perfect():
            break
        continue
    elif sum_values % 5 == 0 and sum_values % 3 != 0:
        willow_fire += 1
        if is_perfect():
            break
        continue
    elif sum_values % 3 == 0 and sum_values % 5 == 0:
        cross_fire += 1
        if is_perfect():
            break
        continue
    else:
        fire_effect.append(firework - 1)
        expl_power.append(explosive)

if is_perfect():
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if fire_effect:
    print(f"Firework Effects left: {', '.join(map(str, fire_effect))}")
if expl_power:
    print(f"Explosive Power left: {', '.join(map(str, expl_power))}")
print(f"Palm Fireworks: {palm_fire}")
print(f"Willow Fireworks: {willow_fire}")
print(f"Crossette Fireworks: {cross_fire}")
