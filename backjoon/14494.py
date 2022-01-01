n,m = list(map(int,input().split()))

dp = [[0] * m for _ in range(n)]

for i in range(m):
    dp[0][i] = 1
for i in range(n):
    dp[i][0] = 1

for i in range(m):
    for j in range(n):
        if dp[j][i] == 0:
            dp[j][i] = dp[j-1][i-1] + dp[j-1][i] + dp[j][i-1]
print(dp[n-1][m-1] % 1000000007)