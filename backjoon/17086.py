from collections import deque

n,m = list(map(int,input().split()))
data = []

dx = [-1, -1, -1, 0, 1, 0, 1, 1]
dy = [-1, 0, 1, 1, 1, -1, 0, -1]

queue = deque()

for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(m):
        if temp[j] == 1:
            queue.append((i,j))
    data.append(temp)

def bfs():
    while queue:
        x,y = queue.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if not data[nx][ny]:
                    queue.append((nx,ny))
                    data[nx][ny] = data[x][y] + 1
    return
bfs()
print(data)
res = 0
for i in range(n):
    for j in range(m):
        res = max(res,data[i][j])
print(res-1)
