import bisect

for _ in range(int(input())):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    res = 0
    for a in A:
        res += (bisect.bisect(B, a-1))
    print(res)