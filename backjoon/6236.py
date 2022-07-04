n,m = list(map(int,input().split()))
money = []
for _ in range(n):
    money.append(int(input()))

start = max(money)
end = sum(money)
res = 0
while start <= end:
    mid = (start+end)//2
    temp = mid
    cnt = 1
    for i in range(n):
        if temp < money[i]:
            temp = mid
            cnt += 1
        temp -= money[i]
    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1
        res = mid
print(res)





