def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

for i in range(1, 101):
    print(f"{i}! = {factorial(i)}")