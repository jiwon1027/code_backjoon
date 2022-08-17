a = input().split('-')
data = []

for i in a:
    cnt = 0
    plus = i.split('+')
    for j in plus:
        cnt += int(j)
    data.append(cnt)

result = data[0]
for i in range(1,len(data)):
    result -= data[i]
print(result)