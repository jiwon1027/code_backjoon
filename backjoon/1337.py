
n = int(input())

data = []

for _ in range(n):
    data.append(int(input()))

res = 5
for i in range(n):
    cnt1=4
    cnt2=4
    for j in range(n):
        if data[i] < data[j] < data[i]+5:
            cnt1 -= 1
        elif data[i]-5 < data[j] < data[i]:
            cnt2 -= 1
    res = min(res, cnt1, cnt2)
print(res)



