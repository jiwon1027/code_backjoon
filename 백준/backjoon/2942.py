r,g = list(map(int,input().split()))


import math
gcd = math.gcd(r,g)


data = []
for i in range(1, gcd//2 + 1):
    if gcd % i == 0:
        data.append(i)
data.append(gcd)

for i in data:
    print(i, r//i, g//i)