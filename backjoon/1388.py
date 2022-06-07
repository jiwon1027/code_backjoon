n,m = list(map(int,input().split()))
data = [list(input()) for _ in range(n)]

res = 0
temp = 0

for i in range(n):
    for j in range(m):
        if data[i][j] == '-':
            temp = 1
        else:
            res += temp
            temp = 0
    else:
        res += temp
        temp = 0

ch_data = list(map(list,zip(*data)))

for i in range(m):
    for j in range(n):
        if ch_data[i][j] == '|':
            temp = 1
        else:
            res += temp
            temp = 0
    else:
        res += temp
        temp = 0
print(res)