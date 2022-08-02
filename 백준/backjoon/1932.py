n = int(input())

data = []
dp = [0] * (n+1)
for _ in range(n):
    data.append(list(map(int,input().split())))
if n == 1:
    print(*data[0])
else:
    data[1][0] = data[1][0] + data[0][0]
    data[1][1] = data[1][1] + data[0][0]

    k = 1

    for i in range(2, n):
        data[i][0] = data[i-1][0] + data[i][0]
        for j in range(1,k+1):
            data[i][j] = max(data[i-1][j-1], data[i-1][j]) + data[i][j]
        data[i][-1] = data[i - 1][-1] + data[i][-1]
        k+=1
    print(max(data[-1]))



