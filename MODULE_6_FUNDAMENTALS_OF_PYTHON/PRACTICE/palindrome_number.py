number = 12345356
temp = number
sum = 0
while number!=0:
    rem = number%10
    sum = (sum*10) + rem
    number=number//10 

    if temp==sum:
        print("palindrome")
    else:
        print("not palindrome")    