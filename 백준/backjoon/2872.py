import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))
res = 0
std = 1

for i in range(n):
    if data[i] > std:
        if data[i] == std+1:
            std = std+1
            continue
        res += data[i]-std
        std = data[i]
print(res)






