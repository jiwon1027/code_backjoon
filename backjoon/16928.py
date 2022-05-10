from collections import deque

def bfs():
    queue = deque()
    queue.append(1)
    visited[1] = 1

    while queue:
        now = queue.popleft()
        for i in range(1,7):
            temp = now + i

            if 0 < temp <= 100 and not visited[temp]:
                if temp in ladder.keys():
                    temp = ladder[temp]

                if temp in snake.keys():
                    temp = snake[temp]

                if not visited[temp]:
                    queue.append(temp)
                    visited[temp] = 1
                    dp[temp] = dp[now] + 1



n,m = list(map(int,input().split()))
dp = [0] * 101
ladder = dict()
snake = dict()

visited = [0] * 101

for _ in range(n):
    a,b = list(map(int,input().split()))
    ladder[a] = b

for _ in range(m):
    a,b = list(map(int,input().split()))
    snake[a] = b

bfs()
#print(dp)
print(dp[100])



