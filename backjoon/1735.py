a,b = map(int,input().split())
c,d = map(int,input().split())


x = a*d + b*c
y = b*d

import math
gcd = math.gcd(x,y)
print(x//gcd, y//gcd)


