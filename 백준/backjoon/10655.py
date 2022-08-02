import sys
input = sys.stdin.readline

def fun(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

data = []
n = int(input())
x,y = list(map(int,input().split()))
data.append([x,y])

total_length = 0
for _ in range(n-1):
    t_x, t_y = list(map(int,input().split()))
    total_length += fun(x,y,t_x,t_y)

    data.append([t_x,t_y])
    x = t_x
    y = t_y

res = total_length

for i in range(1,n-1):
    temp = 0
    prev_x,prev_y = data[i-1][0],data[i-1][1]
    x,y = data[i][0],data[i][1]
    next_x, next_y = data[i+1][0], data[i+1][1]

    temp += fun(prev_x,prev_y,x,y)
    temp += fun(x,y, next_x,next_y)
    temp -= fun(prev_x,prev_y,next_x,next_y)
    res = min(res, total_length - temp)
print(res)











