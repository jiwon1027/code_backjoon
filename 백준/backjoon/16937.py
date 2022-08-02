h,w = list(map(int,input().split()))
n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))

res = 0
for i in range(n-1):
    for j in range(i+1,n):
        r1,c1 = data[i]
        r2,c2 = data[j]

        if (r1 + r2 <= h and max(c1, c2) <= w) or (max(r1, r2) <= h and c1 + c2 <= w):
            res = max(res, r1*c1 + r2*c2)
        if (c1 + r2 <= h and max(r1, c2) <= w) or (max(c1, r2) <= h and r1 + c2 <= w):
            res = max(res, r1*c1 + r2*c2)
        if (c1 + c2 <= h and max(r1, r2) <= w) or (max(c1, c2) <= h and r1 + r2 <= w):
            res = max(res, r1*c1 + r2*c2)
        if (r1 + c2 <= h and max(c1, r2) <= w) or (max(r1, c2) <= h and c1 + r2 <= w):
            res = max(res, r1*c1 + r2*c2)
print(res)