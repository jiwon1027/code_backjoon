# Enter your code here. Read input from STDIN. Print output to STDOUT

H,W,N = list(map(int,input().split()))
board = [list(map(int,input())) for _ in range(H)]

#print(board)

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def dfs(x,y,ans,cnt):
    global maxValue

    if cnt == N:
        maxValue = max(maxValue, ans)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny]:
            if cnt >= 2:
                visited[nx][ny] = 1
                dfs(x,y,ans+board[nx][ny],cnt + 1)
                visited[nx][ny] = 0

            visited[nx][ny] = 1
            dfs(nx, ny, ans + board[nx][ny], cnt + 1)
            visited[nx][ny] = 0


res = []
maxValue = 0

visited = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        visited[i][j] = 1
        dfs(i,j,board[i][j],1)
        visited[i][j] = 0

print(maxValue)




