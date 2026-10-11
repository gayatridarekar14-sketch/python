numbers = [0, 1, 0, 3, 12, 0, 5]

result = []
zero_count = 0

for n in numbers:
    if n != 0:
        result.append(n)
    else:
        zero_count += 1

result += [0] * zero_count

print(result)