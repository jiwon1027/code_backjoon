dp = [0 for _ in range(101)]

for i in range(101):
    if i < 3:
        dp[i] = 1
    elif i < 5 and i > 2:
        dp[i] = 2
    else:
        dp[i] = dp[i-5] + dp[i-1]

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n-1])