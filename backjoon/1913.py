n = int(input())
k = int(input())

data = [[0] * n for _ in range(n)]
x,y = n//2,n//2

data[x][y] = 1 # start 지점

dx = [-1, 0, 1, 0, -1] #상 우 하 좌 상
dy = [0, 1, 0, -1, 0]
k_x, k_y = x ,y
check = 1
i = 2

while i < n**2:
    x += dx[0]
    y += dy[0]
    data[x][y] = i
    if i == k:
        k_x, k_y = x, y
    i += 1



    for _ in range((check * 2) -1):
        x += dx[1]
        y += dy[1]
        data[x][y] = i
        if i == k:
            k_x, k_y = x,y
        i += 1


    for _ in range(check * 2):
        x += dx[2]
        y += dy[2]
        data[x][y] = i
        if i == k:
            k_x, k_y = x,y
        i += 1


    for _ in range(check * 2):
        x += dx[3]
        y += dy[3]
        data[x][y] = i
        if i == k:
            k_x, k_y = x,y
        i += 1


    for _ in range(check * 2):
        x += dx[4]
        y += dy[4]
        data[x][y] = i
        if i == k:
            k_x, k_y = x,y
        i += 1

    check += 1

for i in data:
    print(*i)
print(k_x + 1, k_y + 1)


