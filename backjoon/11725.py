import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] * n for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    for i in graph[start]:
        if not visited[i]:
            visited[i] = start
            dfs(i)
dfs(1)

for x in range(2, n+1):
    print(visited[x])

