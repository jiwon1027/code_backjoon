dx = [1,0]
dy = [0,1]

n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]

def dfs(x,y):
    if 0>x or n<=x or 0>y or n<=y:
        return False
    if visited[x][y]:
        return False
    if x==n-1 and y==n-1:
        print('HaruHaru')
        exit()

    visited[x][y] = 1

    dfs(x+data[x][y],y)
    dfs(x,y+data[x][y])
    return True

visited = [[0] * n for _ in range(n)]
if dfs(0,0):
    print('Hing')