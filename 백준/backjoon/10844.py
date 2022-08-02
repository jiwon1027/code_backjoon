import sys

n = int(sys.stdin.readline())

dp = [[0] * 10 for _ in range(n + 1)]

for i in range(1,10):
    dp[1][i] = 1

# dp[N 자리 수][N자리 숫자일 때 해당 Index 앞에 올 수 있는 일의 자리 수]
for i in range(2, n+1): # n 자리 수
    for j in range(10): # Index
        if j == 0 :
            dp[i][j] = dp[i-1][j+1]
        elif j == 9 :
            dp[i][j] = dp[i-1][j-1]

        # 뒷자리가 2~8일 때는 앞에 숫자가 2개씩 올 수 있음
        else :
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]


print(sum(dp[n]) % 1000000000)