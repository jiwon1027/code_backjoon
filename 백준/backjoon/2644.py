n = int(input())
start,end = list(map(int,input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(int(input())):
    x,y = list(map(int,input().split()))
    graph[x].append(y)
    graph[y].append(x)

from collections import deque
visited = [0] * (n+1)
queue = deque()
queue.append(start)

while queue:
    temp = queue.popleft()
    for i in graph[temp]:
        if not visited[i]:
            if i == end:
                print(visited[temp]+1)
                exit()
            else:
                queue.append(i)
                visited[i] = visited[temp] + 1
else:
    print(-1)



