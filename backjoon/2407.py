n, m = map(int, input().split())
res = 1
res2 = 1

for i in range(m):
    res *= (n-i)
    res2 *= i+1

print(res//res2)
