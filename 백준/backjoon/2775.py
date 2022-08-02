#부녀회장이 될테야

n = int(input())

for _ in range(n):
    k = int(input())
    n = int(input())
    f0 = [x for x in range(1, n+1)]
    for k in range(k):
        for i in range(1, n):
            f0[i] += f0[i-1]
    print(f0[-1])
