def anagram(first, second):
    if len(first) != len(second):
        return False

    count = {}

    for ch in first:
        count[ch] = count.get(ch, 0) + 1

    for ch in second:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False

    return True


print(anagram("listen", "silent"))  # True
print(anagram("hello", "world"))    # False
