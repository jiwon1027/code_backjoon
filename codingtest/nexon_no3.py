n = int(input())
m = int(input())
maze = [list(map(int,input().split())) for _ in range(n)]
x = int(input())
y = int(input())


def minMoves(maze, x, y):
    # Write your code here
    from collections import deque
    from itertools import permutations

    n, m = maze_rows, maze_columns

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    money = []

    for i in range(n):
        for j in range(m):
            if maze[i][j] == 2:
                money.append((i, j))

    def bfs(start, end):
        queue = deque()
        queue.append((start[0], start[1]))

        visited = [[0] * m for _ in range(n)]
        visited[start[0]][start[1]] = 1

        graph = [[0] * m for _ in range(n)]

        while queue:
            a, b = queue.popleft()

            if a == end[0] and b == end[1]:
                return graph[a][b]

            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    if maze[nx][ny] != 1:
                        queue.append((nx, ny))
                        visited[nx][ny] = 1
                        graph[nx][ny] = graph[a][b] + 1
        else:
            return False

    if len(money) == 0:
        if bfs((0, 0), (x, y)) != False:
            return bfs((0, 0), (x, y))
        else:
            return -1
    else:
        res = 0
        ans = []
        for temp in permutations(money):
            temp_list = [(0, 0)] + list(temp) + [(x, y)]
            for i in range(len(temp_list) - 1):
                if bfs(temp_list[i], temp_list[i + 1]) != False:
                    res += bfs(temp_list[i], temp_list[i + 1])
                else:
                    return -1

            ans.append(res)

        return sorted(ans)[0]