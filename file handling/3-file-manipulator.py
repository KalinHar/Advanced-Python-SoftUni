import os


def create(f_name):
    with open(f_name, "w") as file:
        pass


def add(f_name, content):
    with open(f_name, 'a') as file:
        file.write(f"{content}\n")


def replace(f_name, old_str, new_str):
    if os.path.exists(f_name):
        with open(f_name, 'r') as file:
            text = file.read()
            text = text.replace(old_str, new_str)
        with open(f_name, 'w') as file:
            file.writelines(text)
    else:
        print("An error occurred")


def delete(f_name):
    try:
        os.remove(f"{f_name}")
    except FileNotFoundError:
        print("An error occurred")


command = input()
while command != "End":
    action, file_name, *data = command.split("-")
    if action == "Create":
        create(file_name)
    elif action == "Add":
        add(file_name, data[0])
    elif action == "Replace":
        replace(file_name, data[0], data[1])
    elif action == "Delete":
        delete(file_name)
    command = input()
