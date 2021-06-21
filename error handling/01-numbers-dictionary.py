numbers_dictionary = {}

line = input()
while line != "Search":
    try:
        number = int(input())
        numbers_dictionary[line] = number
    except ValueError:
        print("The variable number must be an integer")
    line = input()

line = input()
while line != "Remove":
    if line != "Search":
        # print(numbers_dictionary.get(line, 'Number does not exist in dictionary'))
        try:
            print(numbers_dictionary[line])
        except KeyError:
            print("Number does not exist in dictionary")
    line = input()

line = input()
while line != "End":
    if line != "Remove":
        try:
            del numbers_dictionary[line]
        except KeyError:
            print("Number does not exist in dictionary")
    line = input()

print(numbers_dictionary)
