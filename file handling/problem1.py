from os import path

if path.exists("../files/text.txt"):
    print("File found")
else:
    print("File not found")

# try:
#     open("../files/text.txt")
#     print("File found")
# except FileNotFoundError:
#     print("File not found")