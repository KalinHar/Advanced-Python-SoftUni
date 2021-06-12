from modules.fibonacci.fib_functions import *

command = input()
while command != "Stop":
    command = command.split(" ")
    if command[0] == "Create":
        seq = create_seq(int(command[-1]))
        print(" ".join(map(str, seq)))
    if command[0] == "Locate":
        print(locate(int(command[1]), seq))
    command = input()
