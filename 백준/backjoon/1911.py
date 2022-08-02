n,l = list(map(int,input().split()))
data = []

for _ in range(n):
    data.append(list(map(int,input().split())))
data.sort()

res = 0
start = data[0][0]
for x,y in data:
    temp = 0
    if start < x:
        start = x

    temp = (y-start) // l
    if (y - start) % l:
        temp += 1
    start += temp * l
    res += temp
print(res)
