import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
min_value = sys.maxsize


def dfs_backtracking(start, next, value,visited):
    global min_value

    if len(visited) == n:
        if data[next][start] != 0:
            min_value = min(min_value, value + data[next][start])
        return

    for i in range(n):
        if data[next][i] != 0 and i not in visited and value < min_value:
            visited.append(i)
            dfs_backtracking(start, i, value + data[next][i],visited)
            visited.pop()


for i in range(n):
    dfs_backtracking(i, i, 0, [i])

print(min_value)