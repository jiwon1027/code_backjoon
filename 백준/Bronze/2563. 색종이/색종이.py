n = int(input())

data = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n):
    x,y = list(map(int,input().split()))
    for i in range(x,x+10):
        for j in range(y,y+10):
            data[i][j] = 1
res = 0
for i in data:
    res += i.count(1)
print(res)







