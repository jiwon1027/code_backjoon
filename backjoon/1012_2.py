import sys

import sys
sys.setrecursionlimit(10**6)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x,y):

    if x < 0 or x >= n or y < 0 or y >= m:
        return

    if board[x][y] == 0:
        return

    board[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        dfs(nx,ny)

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
                dfs(i,j)
                res += 1
    print(res)