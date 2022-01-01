import sys
input = sys.stdin.readline #input()
sys.setrecursionlimit(10 ** 6)


n,m = map(int,input().split())

#방향벡터
dx = [-1,0,1,0]
dy = [0,1,0,-1]


board = []
cnt = 0
ia,ib = 0,0
visit = [[0] * m for _ in range(n)]

for i in range(n):
    temp = list(input())
    if 'I' in temp:
        ia,ib = i, temp.index('I')
    board.append(temp)

def dfs(y,x):
    global cnt
    visit[y][x] = 1

    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]

        if not (0 <= b < n and 0 <= a < m):
            continue
        if visit[b][a]:
            continue
        if board[b][a] == 'X':
            continue
        if board[b][a] == 'P':
            cnt += 1
        dfs(b,a)


dfs(ia,ib)
print(cnt if cnt else 'TT')
