
data = list(map(int,input().split()))
dp = [0] * 10000
def fun(num):
    s = str(num)
    res = []
    for _ in range(4):
        res.append(int(s))
        s += s[0]
        s = s[1:]
    return sorted(res)[0]

std = fun(data[0] * 1000 + data[1] * 100 + data[2] * 10 + data[3])
#print(std)

for i in range(1111,std):
    dp[fun(i)] = 1
print(sum(dp[1111:std]) + 1)


