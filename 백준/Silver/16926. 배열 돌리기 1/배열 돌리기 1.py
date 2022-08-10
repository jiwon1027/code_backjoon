from collections import deque

n,m,r = list(map(int,input().split()))
data = [list(map(int,input().split())) for _ in range(n)]

x,y = 0,0
width = m
height = n

#x,y : 배열 왼쪽 상단
#반시계 기준
def rotate(x,y,width,height):
    queue = deque()

    for i in range(y,y+width): #좌
        queue.append(data[x+height-1][i])

    for i in range(x+height-2,x,-1): #상
        queue.append(data[i][y+width-1])

    for i in range(y+width-1,y,-1): #우
        queue.append(data[x][i])

    for i in range(x,x+height-1): #하
        queue.append(data[i][y])
        
    queue.rotate(r)

    for i in range(y,y+width): #좌
        data[x+height-1][i] = queue.popleft()

    for i in range(x+height-2,x,-1): #상
        data[i][y+width-1] = queue.popleft()

    for i in range(y+width-1,y,-1): #우
        data[x][i]  = queue.popleft()

    for i in range(x,x+height-1): #하
        data[i][y]  = queue.popleft()

while True:
    if not width or not height:
        break
    rotate(x,y,width,height)
    x += 1
    y += 1
    width -= 2
    height -= 2

for i in data:
    print(*i)

