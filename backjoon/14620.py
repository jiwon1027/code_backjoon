n = int(input())
cost = []
for _ in range(n):
    cost.append(list(map(int,input().split())))

dx = [0, -1, 0, 1, 0]
dy = [0, 0, -1, 0, 1]

def check(x,y):
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]
        if visited[nx][ny] or nx < 0 or ny < 0 or nx >= n or ny >=n:
            return False
    return True

def dfs(cnt):
    global result, answer

    if cnt == 3:
        answer = min(result, answer)
        return

    for i in range(1, n-1):
        for j in range(1, n-1):
            if check(i,j):
                for k in range(5):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    visited[nx][ny] = 1
                    result += cost[nx][ny]

                dfs(cnt+1)

                for k in range(5):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    visited[nx][ny] = 0
                    result -= cost[nx][ny]

visited = [[0] * n for _ in range(n)]
result = 0
answer = 10000
dfs(0)
print(answer)



