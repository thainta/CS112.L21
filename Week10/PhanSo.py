import math
a = int(input())
b = int(input())
c = int(input())
d = int(input())
result = 0
if a / b > c / d :
    print(0)
else:
    while(a / b < c / d):
      a+=1
      b+=1
      x = math.gcd(a, b)
      a//=x
      b//=x
      if a / b > c / d:
        result = 0
        break 
      result+=1
    print(result)
