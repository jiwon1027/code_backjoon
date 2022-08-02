n,m = list(map(int,input().split()))
data = list(map(int,input().split()))
data.sort()

left = []
right = []
max_value = 0
for i in data:
    if i < 0:
        left.append(-i)
        max_value = max(max_value,-i)
    else:
        right.append(i)
        max_value = max(max_value,i)

res = 0
left = left[::-1]


left_value = len(left) // m
left_remainer = len(left) % m
right_value = len(right) // m
right_remainer = len(right) % m

if left_remainer > 0:
    idx = left_remainer-1
    for i in range(idx,len(left),m):
        res += left[i] * 2
else:
    for i in range(m-1,len(left),m):
        res += left[i] * 2

if right_remainer > 0:
    idx = right_remainer-1
    for i in range(idx,len(right),m):
        res += right[i] * 2
else:
    for i in range(m-1,len(right),m):
        res += right[i] * 2
print(res - max_value)






