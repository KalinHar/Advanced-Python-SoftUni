from collections import deque
commands = deque()
cars = deque()
passed_cars = 0
green_time = int(input())
window_time = int(input())
crash_flag = False


def crash(car, hit):
    global crash_flag
    print("A crash happened!")
    print(f"{car} was hit at {hit}.")
    crash_flag = True


def move_cars(time):
    global passed_cars
    if cars:
        car = cars.popleft()
        passed_cars += 1
        if len(car) < time:
            time -= len(car)
            move_cars(time)
        elif len(car) > time + window_time:
            hit = car[time + window_time]
            crash(car, hit)


command = input()
while command != "END":
    if command != "green":
        cars.append(command)
    else:
        move_cars(green_time)
    if crash_flag:
        break
    command = input()

if not crash_flag:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")
