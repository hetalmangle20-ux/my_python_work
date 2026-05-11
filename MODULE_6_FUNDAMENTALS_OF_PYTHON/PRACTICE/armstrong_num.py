number=153
temp=number
sum=0
while number = 0:
rem = number %10
SUM+= (pow(rem,3))
number=number//10

if temp==sum:
    print(f"{temp} is armstrong")
else:
    print(f"{temp} is not armstrong")