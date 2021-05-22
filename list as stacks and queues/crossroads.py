from collections import deque
commands = deque()
cars = deque()
passed_cars = 0
green_time = int(input())
window_time = int(input())

while True:
    command = input()
    if command != "END":
        commands.append(command)
    else:
        break


def move_cars(c):
    time_to_move = green_time + window_time
    for car in c:
        len_car = len(car)
        if len_car <= time_to_move:



for com in commands:
    if com != "green":
        cars.append(com)
    move_cars(cars)

print(commands)
