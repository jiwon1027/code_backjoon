n,m = map(int,input().split())
board = []
count = []
for _ in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        black_paint = 0
        white_paint = 0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b)%2==0:
                    if board[a][b]!='W':
                        black_paint +=1
                    if board[a][b]!='B':
                        white_paint +=1
                else:
                    if board[a][b]!='B':
                        black_paint +=1
                    if board[a][b]!='W':
                        white_paint +=1
        count.append(min(black_paint,white_paint))

print(min(count))

