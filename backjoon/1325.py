import sys
input = sys.stdin.readline

n,m = list(map(int,input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = list(map(int,input().split()))
    graph[b].append(a)
#print(graph)

from collections import deque
def bfs(i):
    queue = deque()
    visited = [0] * (n+1)
    queue.append(i)
    visited[i] = 1
    cnt = 0

    while queue:
        temp = queue.popleft()
        for j in graph[temp]:
            if visited[j] == 0:
                visited[j] = 1
                queue.append(j)
                cnt += 1
    return cnt


res = []
max_value = -1
for i in range(1,n+1):
    temp = bfs(i)
    if temp > max_value:
        res = [i]
        max_value = temp
    elif temp == max_value:
        res.append(i)
print(*res)