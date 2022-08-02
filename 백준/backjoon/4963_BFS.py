import sys
sys.setrecursionlimit(10**6)
from collections import deque

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    if board[x][y] == 1:
        board[x][y] = 0
        while queue:
            print(queue)
            a, b = queue.popleft()

            for i in range(8):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == 1:

                    board[nx][ny] = 0
                    queue.append([nx,ny])

while True:
    w,h = list(map(int,input().split()))
    if w == 0 and h == 0:
        break
    board = []
    for _ in range(h):
        board.append(list(map(int,input().split())))

    res = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                bfs(i, j)
                res += 1

    print(res)

