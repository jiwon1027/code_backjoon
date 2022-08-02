from collections import deque
def bfs():
    queue = deque()
    queue.append(n)
    while queue:

        v = queue.popleft()
        if v == k:
            print(dp[v])
            break
        for temp in [v - 1,v + 1,2 * v]:
            if 0 <= temp <= MAX and not dp[temp]:
                dp[temp] = dp[v] + 1
                queue.append(temp)



n, k = list(map(int,input().split()))
MAX = 10**5
dp = [0] * (MAX + 1)
bfs()