text = input()
result = {}

for symbol in text:
    if symbol not in result:
        result[symbol] = text.count(symbol)

for k, v in sorted(result.items()):
    print(f'{k}: {v} time/s')
