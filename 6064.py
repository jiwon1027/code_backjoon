import sys

def fun(m, n, x, y):
    while x <= m * n:
        if x%n == y%n:
            return x
        x += m
    return -1

num = int(input())
for _ in range(num):
    m, n, x, y = map(int, sys.stdin.readline().split())
    print(fun(m, n, x, y))

