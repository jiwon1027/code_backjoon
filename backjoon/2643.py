n = int(input())
data = [(1000, 1000)]
ans = 0
for _ in range(n):
    w, h = map(int, input().split())
    data.append((max(w, h), min(w, h)))

data.sort(reverse=True)
print(data)
dp = [[0, data[i][1]] for i in range(n+1)]
#dp[i][0] ==> 몇 장 쌓을 수 있는지
#dp[i][1] ==> 마지막으로 쌓은 길이
for i in range(1, n+1):
    for j in range(i):
        if dp[j][1] >= data[i][1] and dp[j][0] + 1 > dp[i][0]:
            print(dp)

            dp[i][0] = dp[j][0] + 1
            dp[i][1] = data[i][1]
            ans = max(ans, dp[i][0])
print(ans)
