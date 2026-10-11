def process(numbers):
    total = 0
    count = 0
    largest = 0

    for n in numbers:
        if n >= 0 and n % 2 == 0:
            square = n * n
            total += square
            count += 1

            if square > largest:
                largest = square

    if count == 0:
        largest = None

    return total, count, largest


numbers = [-2, 1, 2, 3, 4, 6, -8]

total, count, largest = process(numbers)

print("Total:", total)
print("Count:", count)
print("Largest squared value:", largest)
