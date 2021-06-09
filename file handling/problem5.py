import re


def get_file_content(path):
    with open(path, 'r') as data:
        data = ''.join(data.readlines())
        return pattern.findall(data.lower())


def write_to_file(data):
    for k, v in data:
        output_data = f'{k} - {v}'
        with open('../files/output.txt', 'a') as file:
            file.write(output_data)
            file.write("\n")


pattern = re.compile(r"[a-zA-Z\']+")

path_to_words = '../files/words.txt'
path_to_input = '../files/input.txt'

words = get_file_content(path_to_words)
text = get_file_content(path_to_input)

words_count = {word: text.count(word) for word in words if word in text}
sorted_list = sorted(words_count.items(), key=lambda x: -x[1])

write_to_file(sorted_list)
