def bfs(x,y,arr):
    std = data[x][y]
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and data[nx][ny] == std:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
    if std == 'R':
        arr[0] += 1
    elif std == 'G':
        arr[1] += 1
    else:
        arr[2] += 1


from collections import deque

n = int(input())
data = [list(map(str,input())) for _ in range(n)]

res = [0,0,0]
res2 = [0,0,0]

dx = [-1,0,0,1]
dy = [0,1,-1,0]

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j,res)
#print(sum(res))

for i in range(n):
    for j in range(n):
        if data[i][j] == 'R':
            data[i][j] = 'G'

visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j,res2)
print(sum(res), sum(res2))