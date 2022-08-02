n = int(input())
data = []
for _ in range(n):
    name, day, month, year = input().split()
    data.append([name, int(day), int(month), int(year)])
data.sort(key=lambda x : (-x[3], -x[2], -x[1]))
print(data[0][0])
print(data[-1][0])
