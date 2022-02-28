import sys
input = sys.stdin.readline
def recursive_fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return recursive_fibo(n-2) + recursive_fibo(n-1)


print(recursive_fibo(int(input())))


