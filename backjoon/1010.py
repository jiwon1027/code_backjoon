t = int(input())
for _ in range(t):
    n,m = list(map(int,input().split()))
    if n == m:
        print(1)
    else:
        res = 1
        for i in range(m, m-n, -1):
            res *= i
        for j in range(n, 1, -1):
            res = res // j
        print(res)




