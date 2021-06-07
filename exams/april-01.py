from collections import deque

pizza_orders = deque(map(int, input().split(", ")))
employees = deque(map(int, input().split(", ")))
total_pizzas = 0

while pizza_orders and employees:
    pizzas = pizza_orders.popleft()
    if pizzas not in range(1, 11):
        continue
    employer = employees.pop()
    if pizzas <= employer:
        total_pizzas += pizzas
        continue
    pizza_orders.appendleft(pizzas - employer)
    total_pizzas += employer

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join(map(str, employees))}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(map(str, pizza_orders))}")
