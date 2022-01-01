data = list(map(str,input()))

result = []

def fun(n):
    N=[int(i) for i in str(n)]
    return sum(N)

for i in data:
    for _ in range(fun(ord(i))):
        print(i, end='')
    print()

