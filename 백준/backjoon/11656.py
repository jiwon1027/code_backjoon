data = list(input())
result = []
for i in range(len(data)):
    s = ''
    for j in data[i:]:
        s += j
    result.append(s)
result.sort()

for i in result:

    print(i)