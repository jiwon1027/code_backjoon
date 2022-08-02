import sys
sys.setrecursionlimit(10**6)

n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
def dfs(x,y):
    if x == n-1 and y == n-1:
        return

    x1 = x+board[x][y]
    y1 = y+board[x][y]

    if 0 <= x1 < n:
        dp[x1][y] += dp[x][y]
        dfs(x1, y)

    if 0 <= y1 < n:
        dp[x][y1] += dp[x][y]
        dfs(x, y1)

dfs(0,0)
#print(dp)
print(dp[n-1][n-1])

