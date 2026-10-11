def is_palindrome(text, left=0, right=None):
    
    if right is None:
        right = len(text) - 1

    if left >= right:
        return True

    if text[left] != text[right]:
        return False

    return is_palindrome(text, left + 1, right - 1)


print(is_palindrome("racecar"))  
print(is_palindrome("python"))   