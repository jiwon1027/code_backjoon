#DFS
#일차원배열 visited을 넘겨서 확인

def dfs(start):
    for i in range(n):
        if visited[i] == 0 and board[start][i]:
            visited[i] = 1
            dfs(i)

n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

visited = [0] * n
for i in range(n):
    dfs(i)
    print(*visited) #한 행씩 처리 하기
    visited = [0] * n





