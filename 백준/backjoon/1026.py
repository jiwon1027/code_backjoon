n = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

res = 0

while len(A) != 0:

    min_a = min(A)
    max_b = max(B)
    res += min_a * max_b

    A.remove(min_a)
    B.remove(max_b)
print(res)