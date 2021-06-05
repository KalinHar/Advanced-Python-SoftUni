def get_info(**kwargs):
    name, town, age = kwargs.get("name"), kwargs.get("town"), kwargs.get("age")
    return f"This is {name} from {town} and he is {age} years old"


print(get_info(**{'name': 'George', 'town': 'Sofia', 'age': 20}))
