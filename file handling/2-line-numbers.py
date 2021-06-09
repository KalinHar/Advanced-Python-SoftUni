def get_file_content(path):
    with open(path, 'r') as data:
        return data.readlines()


def write_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data)
        file.write("\n")


read_path = '../files/text.txt'
write_path = '../files/output.txt'

lines = (get_file_content(read_path))

for i in range(0, len(lines)):
    line = lines[i][:-1]
    text = "".join(line.split())
    chars_count = 0
    for char in text:
        if char.isalpha():
            chars_count += 1
    punct_marks = len(text) - chars_count
    new_line = f"Line {i+1}: {line} ({chars_count})({punct_marks})"
    write_to_file(write_path, new_line)

