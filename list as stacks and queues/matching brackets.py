text = input()
brackets_ind = []
for i in range(len(text)):
    if text[i] == "(":
        brackets_ind.append(i)
    elif text[i] == ")":
        print(text[brackets_ind.pop():i+1])
