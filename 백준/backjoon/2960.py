n, k = list(map(int,input().split()))

res = 0
data = [0] * (n+1)

for i in range(2,n+1):
    for j in range(i, n+1, i):
        if not data[j]:
            data[j] = 1
            res += 1
            if res == k:
                print(j)
                exit()


