n = int(input())

data = []
for _ in range(n):
    data.append(list(map(int,input().split())))
data.sort(key = lambda x : -x[2])

print(*data[0][:2])
print(*data[1][:2])

for i in range(2, n):
    if data[0][0] == data[1][0] == data[i][0]:
        continue
    else:
        print(*data[i][:2])
        break

    