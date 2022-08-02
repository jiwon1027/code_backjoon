n,m = list(map(int,input().split()))
board = [list(map(str,input())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

from collections import deque
start_candi = deque()


for i in range(n):
    for j in range(m):
        cnt = 0
        std = board[i][j]
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == std:
                    cnt += 1
        if cnt > 1:
            start_candi.append((i,j))


def bfs(start_x,start_y):
    visited = [[0] * m for _ in range(n)]

    visited[start_x][start_y] = 1
    std = board[start_x][start_y]

    queue = deque()
    queue.append((start_x,start_y))

    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if not visited[nx][ny]:
                if (0 <= nx < n and 0 <= ny < m):
                    if board[nx][ny] == std:
                        visited[nx][ny] = 1
                        queue.append((nx,ny))
            else:
                if nx == start_x and ny == start_y:
                    print(nx, ny)
                    print('Yes')
                    exit()
            print(nx,ny, visited)

def dfs(depth,std,x,y,visited): # 사이클 더 쉽게 돌리는 방법이 있을까..

    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if board[nx][ny] == std:
                dfs(depth+1,std,nx,ny,visited)

        if nx == std_x and ny == std_y and depth > 3:
            print('Yes')
            exit()



while start_candi:
    x,y = start_candi.popleft()
    #bfs(x,y)
    visited = [[0] * m for _ in range(n)]

    std_x, std_y = x,y
    std = board[std_x][std_y]
    dfs(1,std,x,y,visited)
else:
    print('No')