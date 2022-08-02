def fun(n):
    result = 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fun(n-1) + fun(n-2)

n = int(input())

print(fun(n))