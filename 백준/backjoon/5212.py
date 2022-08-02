r,c = list(map(int,input().split()))
board = []

board.append(['.'] * (c+2))
for _ in range(r):
    board.append(['.'] + list(map(str,input())) + ['.'])
board.append(['.'] * (c+2))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
from collections import deque

land = deque()
for i in range(r+2):
    for j in range(c+2):
        if board[i][j] == 'X':
            land.append((i,j))

temp = deque()
def bfs(queue):
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
bfs(land)

# 바다로 바꾸기
while temp:
    a,b = temp.popleft()
    board[a][b] = '.'

# land 좌표 찾기
res = []
for i in range(r+2):
    for j in range(c+2):
        if board[i][j] == 'X':
            res.append((i,j))

# 사각형 꼭짓점 찾기
min_x = sorted(res,key = lambda x: (x[0]))[0][0]
max_x = sorted(res,key = lambda x: (x[0]))[-1][0]

min_y = sorted(res,key = lambda x: (x[1]))[0][1]
max_y = sorted(res,key = lambda x: (x[1]))[-1][1]


for i in range(min_x, max_x + 1):
    for j in range(min_y, max_y + 1):
        print(board[i][j], end= '')
    print()