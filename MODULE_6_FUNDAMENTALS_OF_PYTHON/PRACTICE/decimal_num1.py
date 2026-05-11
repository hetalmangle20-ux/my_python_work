number = 468
st = 0
mul=1
while number !=0:
    rem = number%8
    st = (rem*mul) + st
    number//=8 
    mul*=10
#10100
print(st)