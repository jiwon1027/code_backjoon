n,k = map(int,input().split())
data = []
cnt = 0
for _ in range(n):
    data.append(int(input()))

for i in reversed(range(n)):
    cnt += k // data[i]
    k = k % data[i]

print(cnt)
