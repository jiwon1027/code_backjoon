n, k = list(map(int,input().split()))
data = [list(map(int,input().split())) for _ in range(n)]
ice = [0] * 1000001

for i in range(n):
    ice[data[i][1]] = data[i][0]

window_size = 2*k + 1
window = sum(ice[:window_size])
res = window

for i in range(window_size,1000001):
    window += ice[i] - ice[i-window_size]
    res = max(res,window)
print(res)





