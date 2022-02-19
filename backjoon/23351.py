n, k, a, b = list(map(int, input().split()))
data = [k] * n

day = 0
while True:
    temp = data.index(min(data))
    for i in range(a):
        data[temp + i] += b
    data = [data[i] -1 for i in range(n)]
    day += 1
    if 0 in data:
        print(day)
        exit()
    #print(data)
