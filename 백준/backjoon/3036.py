N = int(input())
data = list(map(int,input().split()))
std = data[0]
import math

for i in data[1:]:
    temp = math.gcd(std,i)
    print(std // temp,end='')
    print('/',end='')
    print(i // temp)



