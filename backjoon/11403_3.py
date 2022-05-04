#bfs
from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        a = queue.popleft()
        for i in range(n):
            if not visited[start][i] and board[a][i]:
                queue.append(i)
                visited[start][i] = 1

n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

visited = [[0] * n for _ in range(n)]
for i in range(n):
    bfs(i)

for i in visited:
    print(*i)