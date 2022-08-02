import sys
input = sys.stdin.readline

def dfs(x,y,ans,cnt):
    global maxValue

    if cnt == 4:
        maxValue = max(maxValue, ans)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if cnt == 2:
                visited[nx][ny] = 1
                dfs(x,y,ans+data[nx][ny],cnt + 1)
                visited[nx][ny] = 0
            visited[nx][ny] = 1
            dfs(nx, ny, ans + data[nx][ny], cnt + 1)
            visited[nx][ny] = 0

n,m = list(map(int,input().split()))
data = [list(map(int,input().split())) for _ in range(n)]
maxValue = 0

dx = [-1,0,0,1]
dy = [0,1,-1,0]
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i,j,data[i][j],1)
        visited[i][j] = 0

print(maxValue)


