dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def check(x,y):
    res = [0] * 8
    std = board[x][y]
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]
        while board[nx][ny]:
            if board[nx][ny] == std:
                nx += dx[k]
                ny += dy[k]
                res[k] += 1
            else:
                break
    for i in range(4):
        if res[i] + res[i+4] == 4:
            return True
    return False

board = [[0] * 21 for _ in range(21)]

n = int(input())
for i in range(1,n+1):
    a,b = list(map(int,input().split()))
    if i % 2 == 1: #홀수(흑)
        board[a][b] = 1
    else: # 짝수(백)
        board[a][b] = 2

    if check(a,b) == True:
        print(i)
        exit()

print(-1)



