
n,m = list(map(int,input().split()))
data = set()
for _ in range(n):
    data.add(input())
res = 0
for _ in range(m):
    if input() in data:
        res += 1
print(res)

