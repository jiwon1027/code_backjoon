n = int(input())

fibo = [0] * 117
fibo[1] = fibo[2] = fibo[3] = 1

for x in range(3,117):
    fibo[x] = fibo[x-1] + fibo[x-3]
print(fibo[n])
