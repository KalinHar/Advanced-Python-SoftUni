bunker = {k: [] for k in input().split(", ")}
count_items = 0
total_quality = 0

for _ in range(int(input())):
    try:
        category, element, qua = input().split(' - ')
        quantity, quality = qua.split(';')
        quantity = int(quantity.split(':')[1])
        quality = int(quality.split(':')[1])
    except:
        continue
    if category in bunker:
        bunker[category].append(element)
        count_items += quantity
        total_quality += quality

print(f"Count of items: {count_items}")
print(f"Average quality: {total_quality / len(bunker):.2f}")
print(*[f"{key} -> {', '.join(value)}" for key, value in bunker.items()], sep="\n")

#
# bunker = {h: {} for h in input().split(", ")}
# total_items = 0
# total_quality = 0
# for _ in range(int(input())):
#     category, item, qua = input().split(" - ")
#     quantity, quality = qua.split(";")
#     quality = int(quality.split(":")[1])
#     quantity = int(quantity.split(":")[1])
#     if not bunker[category].get("item"):  # Without this row
#         total_items += quantity
#         total_quality += quality
#         bunker[category][item] = {"quantity": quantity, "quality": quality}
# print(f"Count of items: {total_items}")
# print(f"Average quality: {total_quality / len(bunker):.2f}")
# print(*[f"{key} -> {', '.join([k for k, v in value.items()])}"for key, value in bunker.items()], sep="\n")
