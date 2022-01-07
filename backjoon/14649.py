p = int(input())
n = int(input())
stone = [0] * 101

for _ in range(n):
    x,y = map(str,input().split())
    x = int(x)

    if y == 'L':
        for i in range(1,x):
            stone[i] += 1
    else:
        for i in range(x+1,101):
            stone[i] += 1

a=0
b=0
c=0

for i in range(1,101):
    if stone[i] % 3 == 0:
        a += 1
    elif stone[i] % 3 == 1:
        b += 1
    elif stone[i] % 3 == 2:
        c += 1

print(format(p * (a/100),'.2f'))
print(format(p * (b/100),'.2f'))
print(format(p * (c/100),'.2f'))
