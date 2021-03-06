def get_file_content(path):
    with open(path, 'r') as data:
        return data.readlines()


path = '../files/text.txt'
set_of_chars = {'.', ',', '-', '!', '?'}

lines = (get_file_content(path))
for i in range(0, len(lines), 2):
    line = lines[i]
    for char in set_of_chars:           # import re
        line = line.replace(char, "@")  # re.sub(r'[-,.!?]', "@", line)
    print(" ".join(reversed(line.split())))

