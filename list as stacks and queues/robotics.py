from collections import deque
from datetime import datetime, timedelta


def robot_on_work():
    current_robot = free_robots.popleft()
    current_robot["ready_time"] = time + timedelta(seconds=current_robot["work_time"])
    robot = [el for el in robots if el == current_robot][0]
    robot["ready_time"] = time + timedelta(seconds=current_robot["work_time"])
    print(f"{robot['name']} - {product} [{time.strftime('%H:%M:%S')}]")


robots_data = input().split(';')
time = datetime.strptime(input(), '%H:%M:%S')

robots = []
free_robots = deque([])
products = deque()

for r in robots_data:
    robot_data = r.split('-')
    robot = {}
    robot["name"] = robot_data[0]
    robot["work_time"] = int(robot_data[1])
    robot["ready_time"] = time
    robots.append(robot)
    free_robots.append(robot)

command = input()
while command != "End":
    products.append(command)
    command = input()

time = time + timedelta(seconds=1)

while len(products) > 0:
    product = products.popleft()

    if free_robots:
        robot_on_work()
    else:
        for r in robots:
            if time >= r['ready_time']:
                free_robots.append(r)

        if not free_robots:
            products.append(product)
        else:
            robot_on_work()

    time = time + timedelta(seconds=1)
