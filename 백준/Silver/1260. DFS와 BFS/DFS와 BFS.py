def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

from collections import deque

def bfs(temp):
    queue = deque()
    queue.append(temp)
    visited[temp] = 0
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if visited[i]:
                queue.append(i)
                visited[i] = 0


n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n+1)
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for row in graph:
    row.sort()

dfs(v)
print()
bfs(v)