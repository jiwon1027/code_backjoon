n = int(input())

data = []
for _ in range(n):
    a,b = list(map(int,input().split()))
    data.append([a,b])
data.sort()

temp = [data[0][1]]

res = 0
for start,end in data:
    for i in range(len(temp)):
        if end not in temp:
            if temp[i] > start:
                res += 1
                temp.append(end)
print(len(temp)-1)