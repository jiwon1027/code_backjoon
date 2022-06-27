h,w,x,y = list(map(int,input().split()))
data = []

for _ in range(h+1):
    data.append(list(map(int,input().split())))

for i in range(x,h):
    for j in range(y,w):
        data[i][j] -= data[i-x][j-y]
for i in range(h):
    for j in range(w):
        print(data[i][j],end=' ')
    print()



