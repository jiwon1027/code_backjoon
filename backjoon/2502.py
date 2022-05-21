d,k = list(map(int,input().split()))

fibo_a = [1,1]
fibo_b = [1,2]
x,y = 0,0

if d == 3:
    x = fibo_a[0]
    y = fibo_b[0]

elif d == 4:
    x = fibo_a[1]
    y = fibo_b[1]

elif d > 4: #3,4일째는 이미 알고있으니까 5일째부터 append하면 됨
    for i in range(d-4):
        fibo_a.append(fibo_a[i] + fibo_a[i+1])
        fibo_b.append(fibo_b[i] + fibo_b[i+1])
    x = fibo_a[-1]
    y = fibo_b[-1]


#print(x,y)
for i in range(1,50001):
    if (k - (x*i)) % y == 0:
        print(i)
        print((k - (x*i)) // y)
        break









