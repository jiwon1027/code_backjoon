data = input()
res = []

for i in range(len(data)-2):
    for j in range(i+1, len(data)-1):
        for k in range(j+1, len(data)):
            temp = data[:j][::-1] + data[j:k][::-1] + data[k:][::-1]
            res.append(temp)
print(min(res))