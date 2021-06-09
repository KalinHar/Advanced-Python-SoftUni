import os

for directory, folders, files in os.walk("."):
    files_dict = {}
    for file in files:
        name, extension = file.split('.')
        if extension not in files_dict:
            files_dict[extension] = [file]
        else:
            files_dict[extension].append(file)

text_dir_info = ""
for ext, f_names in sorted(files_dict.items()):
    text_dir_info += f".{ext}\n"
    for name in sorted(f_names):
        text_dir_info += f"- - - {name}\n"

desktop_path = (os.environ['USERPROFILE'] + '\Desktop')
path = os.path.join(desktop_path, "report.txt")
with open(path, 'w') as file:
    file.write(text_dir_info)

