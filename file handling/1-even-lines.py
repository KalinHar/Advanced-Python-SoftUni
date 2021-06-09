def get_file_content(path):
    with open(path, 'r') as data:
        return data.readlines()


path = '../files/text.txt'

lines = (get_file_content(path))
for i in range(0, len(lines), 2):
    line = lines[i]
    for char in "-,.!?":
        line = line.replace(char, "@")
    print(" ".join(reversed(line.split())))

