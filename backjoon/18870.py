n = int(input())
data = list(map(int,input().split()))

data2 = sorted(list(set(data)))

dict = {data2[i] : i for i in range(len(data2))}
#print(dict)

for i in data:
    print(dict[i], end=' ')

