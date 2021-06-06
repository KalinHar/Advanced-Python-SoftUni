def age_assignment(*names, **ages):
    dict_of_names = {}
    for name in names:
        dict_of_names[name] = ages.get(name[0])
    return dict_of_names


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
