#dfs는 논리상 말이 안됨. 점을 하나 지정해서 길이가 6이 되야하는데 dfs를 해버리면 하나씩 지정이 안됨

import sys

N, K = map(int, sys.stdin.readline().split())
graph = [[] * (N+1) for i in range(N+1)]
check = 0
for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x,cnt):
    visited[x] = 1

    for nx in graph[x]:
        if not visited[nx]:
            dfs(nx,cnt+1)
    return
visited = [0] * (N + 1)
dfs(1,1)

if 0 in visited[1:]:
    print('Big World!')
else:
    print('Small World!')