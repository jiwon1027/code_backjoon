masks = [[3200, 4], [2300, 2], [1100, 1], [4200, 6]]
#masks = [[600, 2], [500, 1], [1015, 400]]
#masks = [[3651, 365], [10, 1]]

dates = ['2022/05/02', '2022/05/01', '2022/05/07', '2022/05/05', '2022/05/08', '2022/05/13~2022/05/15', '2022/05/14~2022/05/17', '2022/05/01~2022/05/02', '2022/05/16']
#dates = ['2023/01/01~2023/01/02', '2021/12/31']
#dates = ["2025/01/01~2025/12/31"]

day = [31,28,31,30,31,30,31,31,30,31,30,31]

data = [[[0] * i  for i in day] for _ in range(10)]

for i in dates:
    if len(i) > 10:
        z1, x1, y1 = int(i[:4]),int(i[5:7]),int(i[8:10])
        z2, x2, y2 = int(i[11:15]),int(i[16:18]),int(i[19:])
        for z in range(z1-2021, 10):
            for x in range(x1-1, 13):
                for y in range(y1-1, day[x]):
                    data[z][x][y] = 1
                    if z == z2 and x == x2 and y == y2:
                        break

    else:
        z1, x1, y1 = int(i[:4]),int(i[5:7]),int(i[8:10])
        print(z1-2021,x1-1,y1-1)
        data[z1-2021][x1-1][y1-1] = 1
res = 0

for i in data:
    for j in i:
        for k in j:
            if k == 1:
                res += 1

print(res)
print(data[1][4])