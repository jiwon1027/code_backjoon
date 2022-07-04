n = int(input())

fibo = [1,1]+ [0] * (n-1)

if n == 1:
    print(4)
elif n == 2:
    print(6)
else:
    for i in range(2,n+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
    #print(fibo)
    print((fibo[n] + fibo[n-1])*2)

