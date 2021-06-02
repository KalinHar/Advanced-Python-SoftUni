# names = {name for name in input().split(', ')}
#
# heroes = {}
# command = input()
# while command != 'End':
#     name, item, cost = command.split('-')
#     cost = int(cost)
#     if name in names:
#         if name not in heroes:
#             heroes[name] = [[item], [cost]]
#         if item not in heroes[name][0]:
#             heroes[name][0].append(item)
#             heroes[name][1].append(cost)
#     command = input()
#
# [print(f"{name} -> Items: {len(heroes[name][0])}, Cost: {sum(heroes[name][1])}") for name in heroes]


heroes = {h: {} for h in input().split(", ")}
line = input()
while line != "End":
    name, item, cost = line.split("-")
    cost = int(cost)
    if not heroes[name].get(item):
        heroes[name].update({item: cost})
    line = input()
[print(f"{key} -> Items: {len(value)}, Cost: {sum([value[price] for price in value])}")
    for key, value in heroes.items()]
