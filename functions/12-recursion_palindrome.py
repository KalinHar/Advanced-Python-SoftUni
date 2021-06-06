def palindrome(word, index=0):
    for i in range(len(word) // 2):
        if word[index] == word[-(index + 1)]:
            if index < len(word) // 2:
                palindrome(word, index + 1)
                return True
            else:return True
        else:return False

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
