n = int(input())
data = []
for _ in range(n):
    data.append(input())
set_temp = set(data)
data = list(set_temp)

data.sort(key = lambda x : (len(x), x))

for i in data:
    print(i)