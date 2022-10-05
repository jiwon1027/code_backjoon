import sys
sys.setrecursionlimit(10**6)

n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for x in range(n):
    for y in range(n):
        if x == n-1 and y == n-1:
            print(dp[x][y])
            exit()

        temp = board[x][y]

        if 0 <= x+temp < n:
            dp[x + temp][y] += dp[x][y]
        if 0 <= y + temp < n:
            dp[x][y + temp] += dp[x][y]





