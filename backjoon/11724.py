import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = list(map(int,input().split()))
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
res = 0
for i in range(m):
    a,b = list(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a)
def dfs(v):
    global res

    visited[v] = 1

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

while True:
    if 0 in visited[1:]:
        dfs(visited[1:].index(0)+1)
        res += 1
    else:
        print(res)
        break

