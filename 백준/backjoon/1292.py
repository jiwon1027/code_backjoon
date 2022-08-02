
a,b = map(int,input().split())
data = [0]
for i in range(1000):
    for j in range(i):
        data.append(i)
print(sum(data[a:b+1]))