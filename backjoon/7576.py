m,n = list(map(int,input().split()))
box = [list(map(int,input().split())) for _ in range(n)]

from collections import deque
q = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append((i,j))
day = 0

def bfs(queue):
    global day
    dx = [-1, 0, 1 ,0]
    dy = [0, 1, 0, -1]

    while queue:
        day += 1
        for _ in range(len(queue)):
            x,y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if not box[nx][ny]:
                        box[nx][ny] = 1
                        queue.append((nx,ny))
bfs(q)
#print(box)
for i in range(n):
    for j in range(m):
        if not box[i][j]:
            print(-1)
            exit()
print(day-1)






