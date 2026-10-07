a = int(input("enter salary 1: "))
b = int(input("enter salary 2: "))
c = int(input("enter salary 3: "))
d = int(input("enter salary 4: "))
e = int(input("enter salary 5: "))

highest = a

if b > highest:
    highest = b

if c > highest:
    highest = c

if d > highest:
    highest = d

if e > highest:
    highest = e


second = 0

if a != highest and a > second:
    second = a

if b != highest and b > second:
    second = b

if c != highest and c > second:
    second = c

if d != highest and d > second:
    second = d

if e != highest and e > second:
    second = e


print("highest salary =", highest)
print("second highest salary =", second)