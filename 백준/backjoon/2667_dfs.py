def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    global res
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    if board[x][y] == 1:
        res += 1
        board[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)
        return 1
    return 0

n = int(input())

board = []
data = []
for _ in range(n):
    board.append(list(map(int,input())))

res = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            if dfs(i,j) == 1:
                data.append(res)
                res = 0

print(len(data))
data.sort()
for i in data:
    print(i)