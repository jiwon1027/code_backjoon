def fun(n):
    temp = 1
    if n>0:
        temp = n * fun(n-1)
    return temp

n = int(input())
print(fun(n))
