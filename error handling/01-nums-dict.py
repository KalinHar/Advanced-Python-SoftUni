def fill_dict(num):
    try:
        numbers_dictionary[line] = int(num)
    except ValueError:
        print("The variable number must be an integer")


def print_value_of_(key):
    try:
        print(numbers_dictionary[key])
    except KeyError:
        print("Number does not exist in dictionary")


def delete_dict_(key):
    try:
        del numbers_dictionary[key]
    except KeyError:
        print("Number does not exist in dictionary")


numbers_dictionary = {}

line = input()
while line != "Search":
    number = input()
    fill_dict(number)
    line = input()

line = input()
while line != "Remove":
    if line != "Search":
        print_value_of_(line)
    line = input()

line = input()
while line != "End":
    if line != "Remove":
        delete_dict_(line)
    line = input()

print(numbers_dictionary)
