from collections import deque

customers = deque(map(int, input().split(", ")))
taxis = deque(map(int, input().split(", ")))
total_time = 0

while customers and taxis:
    customer_time = customers.popleft()
    taxi_time = taxis.pop()

    if customer_time <= taxi_time:
        total_time += customer_time
        continue
    customers.appendleft(customer_time)

if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
else:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(map(str, customers))}")
