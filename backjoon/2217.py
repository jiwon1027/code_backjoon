n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))
data.sort(reverse=True)
for i in range(n):
    data[i] = data[i] * (i+1)
print(max(data))



