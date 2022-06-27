def dfs(v):
    if visited[v]:
        return 0
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
    return 1

for _ in range(int(input())):
    n = int(input())
    data = list(map(int,input().split()))
    std = range(1,n+1)
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)

    cnt = 0
    for i in range(n):
        graph[std[i]].append(data[i])

    for i in range(1,n+1):
        cnt += dfs(i)
    print(cnt)

