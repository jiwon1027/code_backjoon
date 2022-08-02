dx = [1,0,1,-1]
dy = [0,1,1,1]

board = [list(map(int,input().split())) for _ in range(19)]

for x in range(19):
    for y in range(19):
        if board[x][y] != 0:
            std = board[x][y]

            for i in range(4):
                cnt = 1
                nx = x + dx[i]
                ny = y + dy[i]

                while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == std:
                    cnt += 1

                    if cnt == 5:
                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and board[x - dx[i]][y - dy[i]] == std:
                            break
                        if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and board[nx + dx[i]][ny + dy[i]] == std:
                            break
                        print(std)
                        print(x + 1, y + 1)
                        exit(0)

                    nx += dx[i]
                    ny += dy[i]

print(0)