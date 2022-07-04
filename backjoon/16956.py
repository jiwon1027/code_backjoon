r,c = list(map(int,input().split()))
data = []
for _ in range(r):
    data.append(list(map(str,input())))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
flag = False

for i in range(r):
    for j in range(c):
        if data[i][j] == 'W':
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < r and 0 <= ny < c:
                    if data[nx][ny] == 'S':
                        flag = True
                        break
        elif data[i][j] == 'S':
            continue
        else:
            data[i][j] = 'D'
if flag:
    print(0)
else:
    print(1)
    for i in range(r):
        print(''.join(data[i]))