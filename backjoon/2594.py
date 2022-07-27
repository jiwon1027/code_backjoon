time = [[600, 600], [1320, 1320]]
for _ in range(int(input())):
    x, y = input().split()
    x = int(x[:2]) * 60 + int(x[2:]) - 10
    y = int(y[:2]) * 60 + int(y[2:]) + 10
    time.append([x, y])
time.sort()


res = 0
last = 600


for start, end in time:
    res = max(res, start - last)
    last = max(last, end)

    #print(res)
#print(res)