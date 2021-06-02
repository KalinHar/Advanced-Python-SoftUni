lists = list(reversed([[n for n in peace.split()] for peace in input().split("|")]))
flatten_list = [el for sublist in lists for el in sublist]
print(*flatten_list, sep=" ")
