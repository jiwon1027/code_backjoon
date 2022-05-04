#DFS
#다차원배열 visited을 넘겨서 확인

def dfs(std, start):
    for i in range(n):
        if visited[std][i] == 0 and board[start][i]:
            visited[std][i] = 1
            dfs(std, i)

n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

for i in range(n):
    dfs(i,i)

for i in visited:
    print(*i)




