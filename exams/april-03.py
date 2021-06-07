def flights(*args):
    dict_of_flights = {}
    for i in range(0, len(args), 2):
        if args[i] == "Finish":
            return dict_of_flights
        if args[i] in dict_of_flights:
            dict_of_flights[args[i]] += args[i + 1]
        else:
            dict_of_flights[args[i]] = args[i + 1]


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
