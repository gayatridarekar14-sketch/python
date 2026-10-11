def find_missing(numbers, n):
    result = 0
    for i in range(1, n + 1):
        result ^= i
    for x in numbers:
        result ^= x
    return result

print(find_missing([1, 2, 4, 6, 3, 7, 8], 8))  # 5
print(find_missing([2, 3, 4, 5], 5))           # 1