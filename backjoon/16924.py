n,m = list(map(int,input().split()))
board = [list(input()) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
res = []

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def remain_check():
    for i in range(n):
        for j in range(m):
            if dp[i][j] == 1:
                return True
    return False

def check(x,y):
    for s in range(1,m):
        flag = True

        for i in range(4):
            nx = x + dx[i] * s
            ny = y + dy[i] * s
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '*':
                pass
            else:
                flag = False
                break

        if flag:
            dp[x][y] = 0
            for i in range(4):
                nx = x + dx[i] * s
                ny = y + dy[i] * s
                dp[nx][ny] = 0
            res.append((x+1,y+1,s))
        else:
            break

for i in range(n):
    for j in range(m):
        if board[i][j] == '*':
            dp[i][j] = 1


for i in range(1, n-1):
    for j in range(1,m-1):
        if board[i][j] == '*':
            check(i,j)

if remain_check():
    print(-1)
else:
    print(len(res))
    for temp in res:
        print(*temp)








