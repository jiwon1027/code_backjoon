#DFS 이용

import sys

N, K = map(int, sys.stdin.readline().split())
graph = [[] * (N+1) for i in range(N+1)]
check = 0
for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
#print(graph)
def dfs(x,cnt,before):
    if cnt == 7:
        return

    visited[x] = visited[before] + 1
    #print(visited)
    for nx in graph[x]:
        if visited[nx] == -1:
            dfs(nx,cnt+1,x)


for i in range(1, N+1):
    visited = [-1] * (N + 1)
    dfs(i, 0, 0)
    #print('*********')
    if max(visited) > 6 or -1 in visited[1:]:
        check = 1
        break

if not check:
    print('Small World!')
else:
    print('Big World!')
