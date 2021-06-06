def palindrome(word, index):
    if word[index] != word[-(index + 1)]:
        return False
    elif word[index] == word[-(index + 1)] and index == len(word) // 2:
        return True
    else:
        palindrome(word, index + 1)

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
