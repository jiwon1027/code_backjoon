dx = [1,0]
dy = [0,1]

n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]

from collections import deque

queue = deque()
queue.append((0,0))
visited = [[0] * n for _ in range(n)]

while queue:
    x,y = queue.popleft()
    for i in range(2):
        nx = x + dx[i]*data[x][y]
        ny = y + dy[i]*data[x][y]
        if (0<=nx<n) and (0<=ny<n):
            if not visited[nx][ny]:
                if nx == n-1 and ny == n-1:
                    print('HaruHaru')
                    exit()
                else:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
else:
    print('Hing')