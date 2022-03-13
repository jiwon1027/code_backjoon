data = []

for i in range(8):
    data.append([i+1,int(input())])

data.sort(key=lambda x: -x[1])

res = 0
for i in range(5):
    res += data[:5][i][1]
print(res)

temp = data[:5]
temp.sort(key = lambda x : x[0])
#print(temp)
for i in range(5):
    print(temp[i][0], end=' ')



