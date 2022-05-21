n,m,k = list(map(int,input().split()))
cost = list(map(int,input().split()))
friend = [[] for _ in range(n+1)]

for _ in range(m):
    v,w = list(map(int,input().split()))
    friend[v].append(w)
    friend[w].append(v)
print(friend)

from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True

    money = 0

    while queue:
        v = queue.popleft()
        for i in friend[v]:
            print(i)
            if not visited[i]:
                queue.append(i)
                money += cost[i-1]
                visited[i] = True
    print(visited)
    print(money)
    return money

res = sum(cost) + 1
for i in range(1,n+1):
    visited = [0] * (n + 1)
    res = min(res,bfs(i))

if res <= k:
    print(res)
else:
    print('Oh no')