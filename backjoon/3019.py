c,p = list(map(int,input().split()))
init = list(map(int,input().split()))

board = [[0]*c for _ in range(100)]

def shape_settings(p,x,y):
    if p == 5:
        return [[x,y],[x,y+1],[x,y+2],[x-1,y+1]]

for i,val in enumerate(init):
    for idx in range(val):
        board[idx][i] = 1
print(board)
