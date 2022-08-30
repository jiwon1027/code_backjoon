#렉시노스의 가장자리에 위치한 Core는 이미 전원이 연결된 것으로 간주
#전선은 절대로 교차해서는 안 된다

def left_check(x,y):
    dist = 0
    for ny in range(y-1,0,-1):
        if board[x][ny] == 1 and ny == 0:
            break
        dist+=1
    return dist

def right_check(x,y):
    dist = 0
    for ny in range(y,N):
        if board[x][ny] == 1 and ny == N-1:
            break
        dist+=1
    return dist

def top_check(x,y):
    dist = 0
    for nx in range(x-1,0,-1):
        if board[nx][y] == 1 and nx == 0:
            break
        dist+=1
    return dist


for T in range(int(input())):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]

    candi = []

    for i in range(N):
        for j in range(N):
            if i==0 and i==N-1 and j==0 and j==N-1:
                continue
            candi.append((i,j)) #연결해야하는 프로세서 위치 정보


