numbers = [12, 35, 1, 10, 34, 35]

largest = second = None

for n in numbers:
    if largest is None or n > largest:
        second = largest
        largest = n
    elif n != largest and (second is None or n > second):
        second = n

if second is None:
    print("No second-largest distinct value")
else:
    print(second)
