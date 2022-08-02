n = int(input())
ppi = []
for i in range(n):
    w, h = map(int,input().split())

    import math
    ppi.append([i, math.sqrt(w**2 + h**2) / 77])
ppi.sort(key = lambda x : -x[1])
for i in range(n):
    print(ppi[i][0]+1)