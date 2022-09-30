from collections import deque

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, d):
    res = 0
    queue = deque()

    queue.append((x, y, d))
    graph[x][y] = 2
    res += 1

    while queue:
        x, y, d = queue.popleft()
        temp_d = d
        turn = 0
        for i in range(4):
            nd = (temp_d + 3) % 4
            nx = x + dx[nd]
            ny = y + dy[nd]
            temp_d = nd

            if (0 <= nx < n and 0 <= ny < m):
                if (graph[nx][ny] == 0):
                    queue.append((nx, ny, nd))
                    graph[nx][ny] = 2
                    res += 1
                    break
                else:
                    turn += 1

        if (turn == 4): #4방향 청소가 모두 되어있거나 벽이면서
            bx = x + dx[(d + 2) % 4] #반대 방향
            by = y + dy[(d + 2) % 4]
            if (graph[bx][by] == 1):
                return res
            queue.append((bx, by, d))

print(bfs(r, c, d))