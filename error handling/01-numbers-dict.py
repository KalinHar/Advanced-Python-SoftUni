numbers_dictionary = {}
commands = ("Search", "Remove", "End")
line = input()

while line not in commands:
    try:
        number = int(input())
        numbers_dictionary[line] = number
    except ValueError:
        print("The variable number must be an integer")
    line = input()

while line != "End":
    if line == "Search":
        line = input()
        if line not in commands:
            try:
                print(numbers_dictionary[line])
            except KeyError:
                print("Number does not exist in dictionary")
        else:
            continue
    elif line == "Remove":
        line = input()
        if line not in commands:
            try:
                del numbers_dictionary[line]
            except KeyError:
                print("Number does not exist in dictionary")
        else:
            continue
    line = input()

print(numbers_dictionary)
