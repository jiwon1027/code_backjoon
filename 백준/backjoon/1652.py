n = int(input())
data = [input() for _ in range(n)]

res = [0,0]
for i in range(n):
    width , height = 0, 0
    for j in range(n):
        if data[i][j] == '.':
            width += 1
        else:
            width = 0
        if width == 2:
            res[0] += 1

        if data[j][i] == '.':
            height += 1
        else:
            height = 0
        if height == 2:
            res[1] += 1
print(*res)