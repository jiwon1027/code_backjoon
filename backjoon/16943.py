from itertools import permutations

a,b = input().split()
ans = -1
res = []

for i in permutations(a):
    res.append(''.join(i))

for i in res:
    if i[0] != '0':
        i = int(i)
        if i < int(b):
            ans = max(ans,i)
print(ans)
