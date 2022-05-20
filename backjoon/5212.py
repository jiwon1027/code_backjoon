r,c = list(map(int,input().split()))
board = []

board.append(['.'] * (c+2))
for _ in range(r):
    board.append(['.'] + list(map(str,input())) + ['.'])
board.append(['.'] * (c+2))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
from collections import deque

queue = deque()
for i in range(r+2):
    for j in range(c+2):
        if board[i][j] == 'X':
            queue.append((i,j))

def bfs(queue):
    temp = deque()
    while queue:
        a, b = queue.popleft()
        cnt = 0
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if board[nx][ny] == '.':
                cnt += 1
        if cnt >= 3:
            temp.append((a,b))
bfs(queue)

for i in board:
    print(*i)