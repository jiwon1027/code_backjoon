import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()


dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
res = 0
for i in range(1,len(s)+1):
    for j in range(1,len(t)+1):
        if s[i-1] == t[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            if dp[i][j] > res:
                res = dp[i][j]
print(res)