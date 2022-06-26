n = int(input())
data = list(map(int,input().split()))
a,b = list(map(int,input().split()))

from collections import deque

def bfs():
    queue = deque()
    queue.append(a-1)
    dp = [-1] * n
    dp[a-1] = 0

    while queue:
        temp = queue.popleft()
        for k in range(temp,n,data[temp]):
            if dp[k] == -1:
                queue.append(k)
                dp[k] = dp[temp] + 1
                #print(dp)
                if k == b-1:
                    return dp[k]
        for k in range(temp,-1,-data[temp]):
            if dp[k] == -1:
                queue.append(k)
                dp[k] = dp[temp] + 1
                if k == b-1:
                    return dp[k]
    return -1
print(bfs())
