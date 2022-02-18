import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
visited = [0] * (n+1)
graph = [[] * n for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 0

def dfs(start):
    global cnt
    visited[start] = 1

    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            cnt += 1

dfs(1)
print(cnt)