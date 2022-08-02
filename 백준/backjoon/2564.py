w,h = list(map(int,input().split()))
road = [0] * 2*(w+h)
n = int(input())
for i in range(n+1):
    direct, x = list(map(int,input().split()))
    if direct == 1:
        road[x] = i+1
    elif direct == 4:
        road[w+x] = i+1
    elif direct == 2:
        road[w+h+w-x] = i+1
    elif direct == 3:
        road[w+w+h+h-x] = i+1

std = road.index(n+1)
res = 0
temp = []
for i in range(len(road)):
    if road[i] != 0 and i != std:
        temp.append(i)

for k in temp:
    if std < k:
        if k-std < len(road)-k+std:
            res += k-std
        else:
            res += len(road)-k+std
    else:
        if std-k < len(road)-std+k:
            res += std-k
        else:
            res += len(road)-std+k
print(res)

