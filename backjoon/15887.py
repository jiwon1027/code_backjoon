n = int(input())
data = list(map(int,input().split()))

import copy
data_temp = copy.deepcopy(data)
data_temp.sort()
result = []
i = 1
cnt = 0

while data != data_temp:
    if data[i-1] != i:
        cnt += 1
        k = data.index(i) + 1
        data[i-1:data.index(i)+1] = data[i-1:data.index(i)+1][::-1]
        result.append([i,k])
    i += 1
print(cnt)

for i in result:
    print(*i)