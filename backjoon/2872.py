n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))
cnt = 0
for i in reversed(range(n)):
    print(data)

    if data[i] != i+1:
        data = [data.pop(i)] + data
        cnt += 1
    print(data)

print(cnt)






