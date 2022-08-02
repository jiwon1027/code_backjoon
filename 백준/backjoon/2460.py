res = 0
data = []
for _ in range(10):
    a,b = list(map(int,input().split()))
    res -= a
    res += b

    data.append(res)
print(max(data))


