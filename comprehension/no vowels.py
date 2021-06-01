text = input()
vowels = {'a', 'o', 'u', 'e', 'i'}
vowels = vowels.union({x.upper() for x in vowels})
result = [x for x in text if x not in vowels]
print("".join(result))
