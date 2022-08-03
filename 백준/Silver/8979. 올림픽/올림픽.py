n,k = list(map(int,input().split()))
data = []
for i in range(1,n+1):
    data.append(list(map(int,input().split())))
data.sort(key=lambda x : (-x[1],-x[2],-x[3]))
idx = 0
for i in range(n):
    if data[i][0] == k:
        idx = i
for i in range(n):
    if data[idx][1:] == data[i][1:]:
        print(i+1)
        break

