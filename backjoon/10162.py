t = int(input())
data = [300, 60, 10]

res = []
res.append(t // data[0])
res.append((t % data[0]) // data[1])
res.append((t % data[0]) % data[1] // data[2])

ans = 0
for i in range(3):
    ans += res[i] * data[i]
if ans == t:
    print(*res)
else:
    print(-1)