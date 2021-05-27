text = input()
result = {}

for symbol in text:
    if symbol not in result:
        result[symbol] = text.count(symbol)
    # result[symbol] = result.get(symbol, 0) + 1

for k, v in sorted(result.items()):
    print(f'{k}: {v} time/s')
