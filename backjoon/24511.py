import sys
input = sys.stdin.readline

n = int(input())
queuestack = list(map(int, input().split()))
B = list(map(int, input().split()))

m = int(input())
C = list(map(int, input().split()))

res = []
for j in C:
    temp = j
    for i in range(n):
        if queuestack[i] == 0:
            data = temp
            temp = B[i]
            B[i] = data
    res.append(temp)
print(*res)
