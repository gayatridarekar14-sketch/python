number = int(input("Enter a number: "))

original_num = number
reverse = 0

while number != 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

if original_num == reverse:
    print("num is palindrome")
else:
    print("num not a palindrome")