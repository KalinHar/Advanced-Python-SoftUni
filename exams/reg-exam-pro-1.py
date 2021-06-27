from collections import deque

chocolates = deque(map(int, input().split(', ')))
milk_cups = deque(map(int, input().split(', ')))

milkshakes = 0

while milk_cups and chocolates:
    milk = milk_cups.popleft()
    choco = chocolates.pop()
    if milk <= 0 and choco <= 0:
        continue
    elif choco <= 0:
        milk_cups.appendleft(milk)
        continue
    elif milk <= 0:
        chocolates.append(choco)
        continue

    if milk == choco:
        milkshakes += 1
        if milkshakes == 5:
            break
    else:
        milk_cups.append(milk)
        chocolates.append(choco - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print("Chocolate: empty")
if milk_cups:
    print(f"Milk: {', '.join(map(str, milk_cups))}")
else:
    print("Milk: empty")
