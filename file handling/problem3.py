import os

with open("../files/asd.txt", "r") as file:
    for line in file:
        print(line, end='')

# try:
#     os.remove("../files/asd.txt")
# except FileNotFoundError:
#     print("file already deleted")


current_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_dir, "..", "files", "text.txt")

print(__file__)
print(current_dir)
print(path)

