def palindrome(word, index):
    if index == len(word) // 2:
        return f"{word} is a palindrome"
    elif word[index] != word[-(index + 1)]:
        return f"{word} is not palindrome"
    return palindrome(word, index + 1)

    # if word[index] != word[-(index + 1)]:
    #     return f"{word} is not palindrome"
    # elif index < len(word) // 2:
    #     palindrome(word, index+1)
    # return f"{word} is a palindrome"

    # for _ in range(len(word) // 2):
    #     if word[index] != word[-(index + 1)]:
    #         return f"{word} is not palindrome"
    #     index += 1
    # return f"{word} is a palindrome"


print(palindrome("abaaba", 0))
print(palindrome("ababa", 0))
print(palindrome("petcep", 0))
print(palindrome("peter", 0))
