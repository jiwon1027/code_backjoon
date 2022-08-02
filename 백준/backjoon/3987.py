def move(x,y,flag):
    if flag == 'U': #up
        return x - 1, y
    elif flag == 'R': #down
        return x, y + 1
    elif flag == 'D': #left
        return  x + 1, y
    elif flag == 'L': #right
        return x, y - 1


n,m = list(map(int,input().split()))
board = [list(map(str,input())) for _ in range(n)]
pr,pc = list(map(int,input().split()))

res = dict()
res['U'] = 0
res['D'] = 0
res['L'] = 0
res['R'] = 0


for direction in ['U','R','D','L']:
    x, y = pr - 1, pc - 1
    start_x, start_y = x,y
    time = 0
    flag = direction
    while True:
        if not (0 <= x < n and 0 <= y < m) or board[x][y] == 'C':
            break

        if board[x][y] == '/' and flag == 'U':
            flag = 'R'
        elif board[x][y] == '\\' and flag == 'U':
            flag = 'L'

        elif board[x][y] == '/' and flag == 'D':
            flag = 'L'
        elif board[x][y] == '\\' and flag == 'D':
            flag = 'R'

        elif board[x][y] == '/' and flag == 'L':
            flag = 'D'
        elif board[x][y] == '\\' and flag == 'L':
            flag = 'U'

        elif board[x][y] == '/' and flag == 'R':
            flag = 'U'
        elif board[x][y] == '\\' and flag == 'R':
            flag = 'D'

        x,y = move(x,y,flag)
        res[direction] += 1

        if x == start_x and y == start_y and flag == direction :
            print(direction)
            print('Voyager')
            exit()


#print(res)
for k,v in res.items():
    if v == max(res.values()):
        print(k)
        print(v)
        break


