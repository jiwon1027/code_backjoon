r,c = list(map(int,input().split()))

board = [list(map(str,input())) for _ in range(10)]
visit = [[0] * 10 for i in range(10)]


def fun(y,x):
    for i in range(10):
        if visit[i][x] == 0 and board[i][x] == 'x':
            board[i][x] = 'o'
            visit[i][x] = 1

        if visit[y][i] == 0 and board[y][i] == 'x':
            board[y][i] = 'o'
            visit[y][i] = 1

for y in range(10):
    for x in range(10):
        if board[y][x] == 'o' and visit[y][x] == 0:
            fun(y,x)
result = []



for y in range(10):
    for x in range(10):
        if board[y][x] == 'x':
            result.append(abs(y+1-r) + abs(x+1-c))

print(min(result))
