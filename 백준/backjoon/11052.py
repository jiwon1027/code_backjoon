n = int(input())
dp = [0] * (n+1)
data = [0] + list(map(int,input().split()))
dp[1] = data[1]

for i in range(2,n+1):
    for j in range(1,i+1):
        if dp[i] < dp[i-j] + data[j]:
            dp[i] = dp[i - j] + data[j]

print(dp[n])