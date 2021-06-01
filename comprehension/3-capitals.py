result = zip([country for country in input().split(", ")], [capital for capital in input().split(", ")])
for r in result:
    print(f"{r[0]} -> {r[1]}")

# [print(f"{r[0]} -> {r[1]}") for r in zip([country for country in input().split(", ")], [capital for capital in input().split(", ")])]