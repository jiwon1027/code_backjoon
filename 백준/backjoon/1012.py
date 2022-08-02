from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    board[x][y] = 0
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny <0 or ny >=m:
                continue
            if board[nx][ny]:
                board[nx][ny] = 0
                queue.append((nx,ny))
    return

t = int(input())
for _ in range(t):
    m,n,k = list(map(int,input().split()))
    board = [[0] * m for _ in range(n)]
    data = []
    for _ in range(k):
        data.append(list(map(int,input().split())))
    for x,y in data:
        board[y][x] = 1

    res = 0
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                bfs(i,j)
                res += 1
    print(res)


