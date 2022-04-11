from itertools import permutations

x = list(input())
data = list(permutations(x,len(x)))

data.sort()
res = []
for i in data:
    res.append(''.join(i))


origial = ''.join(x)
idx = res.index(origial)

for i in range(idx, len(res)):
    if int(res[i]) > int(origial):
        print(res[i])
        break
else:
    print(0)
