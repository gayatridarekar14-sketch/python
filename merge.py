def merge(a, b):
    i = j = 0
    result = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result += a[i:]
    result += b[j:]

    return result


a = [1, 4, 7, 10]
b = [2, 3, 8, 11, 15]

print(merge(a, b))
