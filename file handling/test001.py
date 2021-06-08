import os

try:
    a = open("..files/example.txt", "w")  # write mode - remove info before write
    b = open("..files/example.txt", "a")  # write/append mode - append info write
    c = open("..files/example.txt", "+")  # read and write/append mode - append info write
    a.write("Hello")
except FileNotFoundError:
    print("File is not found!")


