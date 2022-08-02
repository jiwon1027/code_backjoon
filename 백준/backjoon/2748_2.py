fibo = []
n = int(input())
res = 0

for i in range(n+1):
    if i == 0:
        res = 0
    elif i <= 2:
        res = 1
    else:
        res = fibo[-1] + fibo[-2]
    fibo.append(res)
print(fibo[-1])