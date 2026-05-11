number = 155
st = ""
while number !=0:
     rem = number%2
     st = str(rem) + st
     number//=2  
     print(st)
