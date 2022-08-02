from collections import deque
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs(queue):
    global day
    while queue:
        day += 1
        for _ in range(len(queue)):
            z, x, y = queue.popleft()
            for i in range(6):
                nz = z + dz[i]
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nz < h and 0 <= nx < n  and 0 <= ny < m:
                    if not box[nz][nx][ny]:
                        box[nz][nx][ny] = 1
                        queue.append((nz,nx,ny))

m,n,h = list(map(int,input().split()))
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
day = 0
q=deque()

for z in range(h):
    for i in range(n):
        for j in range(m):
            if box[z][i][j] == 1:
                q.append((z,i,j))
bfs(q)

for z in range(h):
    for i in range(n):
        for j in range(m):
            if not box[z][i][j]:
                print(-1)
                exit(0)
print(day-1)




