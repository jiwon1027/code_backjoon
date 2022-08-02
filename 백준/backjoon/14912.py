n, d = list(map(int,input().split()))

data = list(range(1, n+1))

data = list(map(str,data))

res = 0
for i in data:
    if str(d) in i:
       res += i.count(str(d))
print(res)