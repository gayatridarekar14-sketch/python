from functools import reduce

n = [1,2,3,4,5,6,7,8,9]

R = list(filter(lambda x: x % 2 == 0, n))
print(R)

result = list(map(lambda x: x**2, R))
print(result)

sum = reduce(lambda a,b: a+b, result)
print(sum)