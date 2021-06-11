def get_file_content(path):
    with open(path, 'r') as data:
        return data.readlines()


def write_to_file(path, data):
    with open(path, 'a') as file:
        file.writelines(data)


read_path = '../files/text.txt'
write_path = '../files/output.txt'

lines = (get_file_content(read_path))
output_lines = []

for i in range(0, len(lines)):
    line = lines[i].strip()
    text = "".join(line.split())

    chars_count = len([char for char in text if char.isalpha()])
    punct_marks = len(text) - chars_count

    new_line = f"Line {i+1}: {line} ({chars_count})({punct_marks})\n"
    output_lines.append(new_line)

write_to_file(write_path, output_lines)

