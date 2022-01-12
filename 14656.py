n = int(input())
data = list(map(int,input().split()))

import copy
temp = copy.deepcopy(data)
data.sort()
cnt = 0
for i in range(n):
    if not temp[i] == data[i]:
        cnt+=1
print(cnt)