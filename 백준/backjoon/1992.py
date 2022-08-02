n = int(input())

data = [list(map(int,input())) for _ in range(n)]
res = []
def divide(x,y,n):
    std = data[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if std != data[i][j]:
                res.append('(')
                for a in range(2):
                    for b in range(2):
                        divide(x + a*n//2, y + b*n//2,n//2)
                res.append(')')
                return
    res.append(std)
divide(0,0,n)
for i in res:
    print(i, end='')

