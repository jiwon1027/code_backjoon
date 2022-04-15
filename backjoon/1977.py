m = int(input())
n = int(input())

res = []
for i in range(m, n+1):
    if not (i ** 0.5) % 1:
       res.append(i)
if not len(res):
    print(-1)
else:
    print(sum(res))
    print(res[0])

