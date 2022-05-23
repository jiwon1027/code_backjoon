import sys
input = sys.stdin.readline

from bisect import bisect_left
t = int(input())
for _ in range(t):
    n,m = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    B.sort()
    #print(B)
    res = 0
    for num in A:
        idx = bisect_left(B,num)
        #print(num,idx)
        if idx >= len(B):
            res += B[idx - 1]
        else:
            if abs(num - B[idx-1]) > abs(num - B[idx]):
                res += B[idx]
            else:
                res += B[idx-1]
    print(res)




