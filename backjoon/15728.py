n, k = list(map(int,input().split()))

share = list(map(int,input().split()))
team = list(map(int,input().split()))

for _ in range(k):
    s = -int(1e9)
    x = 0
    for i in team:
        for j in share:
            if s <= i * j:
                s = i * j
                x = i
    team.remove(x)
ans = -int(1e9)
for i in team:
    for j in share:
        ans = max(ans, i*j)
print(ans)
