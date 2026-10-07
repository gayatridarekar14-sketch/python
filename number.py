n = int(input("Enter a number: "))

numbers = [12,12,2,6,677]

for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

print("Numbers:", numbers)

largest = numbers[0]
smallest = numbers[0]
total = 0

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

    total = total + num

average = total / n

print("Largest number:", largest)
print("Smallest number:", smallest)
print("Total Sum:", total)
print("Average:", average)