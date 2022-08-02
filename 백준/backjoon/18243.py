#BFS 이용

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
graph = [[] * (N+1) for i in range(N+1)]
check = 0
for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
#print(graph)

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 0

    while q:
        x = q.popleft()
        for nx in graph[x]:
            if visited[nx] == -1:
                q.append(nx)
                visited[nx] = visited[x] + 1
    return

for i in range(1, N+1):
    visited = [-1] * (N + 1)
    bfs(i)
    print(visited)
    if max(visited) > 6 or -1 in visited[1:]:
        check = 1
        break

if not check:
    print('Small World!')
else:
    print('Big World!')