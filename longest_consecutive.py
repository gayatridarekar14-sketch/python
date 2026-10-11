def longest_run(numbers):
    if not numbers:
        return 0

    max_count = 1
    current = 1

    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            current += 1
        else:
            current = 1

        if current > max_count:
            max_count = current

    return max_count

print(longest_run([1, 1, 2, 2, 2, 3, 3, 1, 1, 1, 1]))  
print(longest_run([7, 7, 7, 7]))                        