n = int(input())
data = list(map(int,input().split()))
res = 0

def fun(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)

for idx, b in enumerate(data):
    temp = 0
    left_max = 1000000000
    right_max = -1000000000

    #left, 기울기가 계속 작아져아함
    for i in range(idx-1,-1,-1):
        c = fun(idx,b,i,data[i])
        if c < left_max:
            left_max = c
            temp += 1

    #right, 기울기가 계속 커져야함
    for i in range(idx+1,n):
        c = fun(idx,b,i,data[i])
        if c > right_max:
            right_max = c
            temp += 1

    res = max(res,temp)
print(res)