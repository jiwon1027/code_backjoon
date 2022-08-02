n,k = list(map(int,input().split()))
exp = list(map(int,input().split()))
exp.sort()

res = 0
use_cnt = 0
for i in range(n):
    res += use_cnt * exp[i]
    if use_cnt < k:
        use_cnt += 1
print(res)


