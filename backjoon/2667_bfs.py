from collections import deque

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))
    board[x][y] = 0
    res = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if board[nx][ny] == 1:
                board[nx][ny] = 0
                queue.append((nx, ny))
                res += 1
    return res

n = int(input())

board = []
data = []
for _ in range(n):
    board.append(list(map(int,input())))
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            data.append(bfs(i, j))
data.sort()

print(len(data))
for i in range(len(data)):
    print(data[i])