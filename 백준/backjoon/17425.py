import sys
input=sys.stdin.readline

dp = [0] * 1000001

#n = int(input())

for j in range(1, 1000001):
    temp = 0
    for i in range(1, j+1):
        temp += (j//i)*i
    dp[j] = temp


print(dp)