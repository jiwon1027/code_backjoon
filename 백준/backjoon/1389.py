def bfs(start):
    visited = [start]
    data = [0] * (n + 1)

    queue = deque()
    queue.append(start)

    while queue:
        a = queue.popleft()
        for i in friend[a]:
            if i not in visited:
                data[i] = data[a] + 1
                visited.append(i)
                queue.append(i)
    #print(visited)
    return sum(data)

n, m = list(map(int,input().split()))
friend = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = list(map(int,input().split()))
    friend[a].append(b)
    friend[b].append(a)

from collections import deque


res = []
for i in range(1, n+1):
    res.append(bfs(i))
print(res.index(min(res)) + 1)

