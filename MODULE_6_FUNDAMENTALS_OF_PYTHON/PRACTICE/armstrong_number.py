number = int(input("Enter a number: "))

num = number
digits = len(str(number))
sum = 0

while num > 0:
    digit = num % 10
    sum += digit ** digits
    num //= 10

if sum == number:
    print("Armstrong number")
else:
    print("Not an Armstrong number")