n = int(input())
a,b = list(map(int,input().split()))
c = int(input())

d = []
for _ in range(n):
    d.append(int(input()))

d.sort(reverse=True)

res = c/a

for k in range(n):
    temp = (c + sum(d[:k+1])) / (a + b * (k + 1))
    if temp < res:
        break
    else:
        res = temp
print(int(res))