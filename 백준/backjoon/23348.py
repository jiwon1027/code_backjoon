a,b,c = list(map(int, input().split()))
n = int(input())
res = []
for _ in range(n):
    data = []
    temp = 0
    for _ in range(3):
        data = list(map(int, input().split()))
        temp += data[0] * a
        temp += data[1] * b
        temp += data[2] * c
    res.append(temp)
print(max(res))