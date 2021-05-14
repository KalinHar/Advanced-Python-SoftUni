quantity_of_food = int(input())
orders = [int(x) for x in input().split()]
print(max(orders))
left_orders = []

while orders:
    if quantity_of_food >= orders[0]:
        quantity_of_food -= orders[0]
        orders.remove(orders[0])
    else:
        left_orders = orders
        orders = []

if left_orders:
    print(f"Orders left: {' '.join([str(x) for x in left_orders])}")
else:
    print('Orders complete')
